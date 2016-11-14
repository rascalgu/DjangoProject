from django import forms
from .models import Project

class AddProjectForm(forms.Form):
    project_name = forms.CharField(max_length=200, null=True, blank=True)
    class Meta:
        model = Project