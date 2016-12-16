from django import template 
register = template.Library()
from .. import forms
from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth.views import login

@register.inclusion_tag('accounts/registration.html')
def registration():
	form = forms.UserRegistrationForm()
	return ({'form':form})


@register.inclusion_tag('registration/login.html')
def loginform():
	form = AuthenticationForm()
	return ({'form':form})
	