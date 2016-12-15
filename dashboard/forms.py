from django import forms
from projects.models import Project


class BasicsForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['name', 'desc', 'goal', 'img']