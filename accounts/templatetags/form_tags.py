from django import template 
register = template.Library()
from .. import forms

@register.inclusion_tag('registration/registration.html')
def registration():
	form = forms.UserRegistrationForm()
	return ({'form':form})