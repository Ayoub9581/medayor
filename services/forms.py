from django import forms
from .models import Service
from domains.models import Domain
from pagedown.widgets import PagedownWidget



class ServiceForm(forms.ModelForm):
    description_service = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = Service
        fields  = ('nom_service','description_service','image_service','domain_service','is_draft')
        widgets = {
                'nom_service':forms.TextInput(attrs={'class':'form-control','type':'text'}),
                'is_draft':forms.CheckboxInput(attrs={'class':'filled-in chk-col-deep-purple','id':'md_checkbox_24','type':'checkbox'}),
                'description_service':forms.Textarea(attrs={'class':'form-control no-resize'}),
        }
