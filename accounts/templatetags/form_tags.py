from django import template 
register = template.Library()
from .. import forms
from django.contrib.auth.forms import AuthenticationForm

@register.inclusion_tag('accounts/registration.html')
def registration():
	form = forms.UserRegistrationForm()
	return ({'form':form})


#@register.inclusion_tag('registration/login.html')
@register.inclusion_tag('registration/login.html')
def login():
	log = AuthenticationForm()
	return ({'log':log})