# -*- coding: utf-8 -*-
from django import forms
from .models import Project

class ProjectForm(forms.Form):
    project_name = forms.CharField(max_length=200)

    class Meta:
        model = Project