from django import forms
from django.contrib.auth.models import User

from .models import Project, Label


class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['project_name']


class LabelForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ['label_title', 'macro_type']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']