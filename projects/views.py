from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Project (View):
	def get(self, request):
		template_name= 'preject.html'
		return render(request, template_name)
