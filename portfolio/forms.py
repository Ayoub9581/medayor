from django import forms




class ProjectForm(forms.Form):

    class Meta:
        fields = ('project_name','domaine', 'annee','description')
