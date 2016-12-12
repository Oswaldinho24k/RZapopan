from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class Projects (View):
	def get(self, request):
		template_name= 'projects.html'
		return render(request, template_name)
