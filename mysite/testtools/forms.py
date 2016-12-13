# -*- coding: utf-8 -*-
from django import forms
from .models import Project,Message

class ProjectForm(forms.Form):
    project_name = forms.CharField(max_length=200)

    class Meta:
        model = Project

class MessageForm(forms.Form):
    name = forms.CharField(max_length=50)
    Email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Message