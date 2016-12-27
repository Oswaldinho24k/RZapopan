from django import forms
from projects.models import Project
from accounts.models import Profile


class ImgForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['img','tel']

class BasicsForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['name', 'desc', 'goal', 'img','video']

class HistoryForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['desc','video','img']