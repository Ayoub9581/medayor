from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name','email','note',)
        widgets = {
        'name':forms.TextInput(attrs={'class':'form-control','type':'text'}),
        'email':forms.TextInput(attrs={'class':'form-control','type':'text'}),
        'note':forms.Textarea(attrs={'class':'form-control no-resize',
        'placeholder':'envoyez-nous un message.. ',
        'rows':'4'}),


        }
