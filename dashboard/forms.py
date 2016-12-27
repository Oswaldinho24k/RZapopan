from django import forms
from projects.models import Project, Reward
from accounts.models import Profile


class ImgForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['img','tel']

class BasicsForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['name', 'goal']

class HistoryForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['desc','video','img']

class NewRewardForm(forms.ModelForm):
	class Meta:
		model = Reward
		fields = ['title','price','desc','quantity','deliver_date']