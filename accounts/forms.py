from django import forms
from .models import MyUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model, authenticate
from django.core.validators import RegexValidator
from django.db.models  import Q

User = get_user_model()

class UserLoginForm(forms.Form):
    query = forms.CharField(label='username/email',
    widget=forms.TextInput(attrs={'class' : 'form-control' , 'placeholder':'username'}))
    password = forms.CharField(label='password',
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'password'}))

    def clean(self, *args, **kwargs):
        query = self.cleaned_data.get('query')
        password = self.cleaned_data.get('password')
        user_qs_final = User.objects.filter(
            Q(username__iexact=query) | Q(email__iexact=query)
        ).distinct()
        if not user_qs_final.exists() and user_qs_final.count() != 1:
            raise forms.ValidationError('Invalide Credentials -- username')
        user_obj = user_qs_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError('Invalide Credentials -- Password')
        if not user_obj.is_active:
            raise forms.ValidationError('Inactive User!, please verify your email address ')

        self.cleaned_data['user_obj'] = user_obj
        return super(UserLoginForm, self).clean(*args, **kwargs)

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',
    widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder':'password'}))
    password2 = forms.CharField(label='Password confirmation',
     widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder':'password confirmation'}))

    class Meta:
        model = User
        fields = ('username', 'email')
        widgets = {
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}),
        }
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.is_active = True
        #TODO , make is_active False and generate a hash Code to acive user account
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password  = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username','email', 'password', 'is_staff', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
