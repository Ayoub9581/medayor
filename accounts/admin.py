from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import MyUser
from .forms import UserCreationForm, UserChangeForm

# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username','email','is_admin','is_active')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('username','email', 'password')}),
        ('Permissions', {'fields':('is_admin','is_staff','is_active')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )

    search_fields = ('username', 'email',)
    ordering = ('username', 'email',)
    filter_horizontal = ()

admin.site.register(MyUser, UserAdmin)
# admin.site.register(Profile)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
