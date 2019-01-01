from django import forms
from .models import Project



class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('project_name','domaine_project', 'annee','description','technologies_project','draft',)
        widgets = {
            'project_name':forms.TextInput(attrs={'class':'form-control'}),
            'technologies_project':forms.TextInput(attrs={'class':'form-control','type':'text','data-role':'tagsinput','type':'text'
            ,'value':'java'}),
            'description':forms.Textarea(attrs={'class':'form-control no-resize'}),
            'draft':forms.CheckboxInput(attrs={'class':'filled-in chk-col-deep-purple','id':'md_checkbox_24','type':'checkbox'}),
            'annee':forms.TextInput(attrs={'class':'form-control','placeholder':'choose date'}),
        }
