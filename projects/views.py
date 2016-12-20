from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Project

# Create your views here.

class Projects (View):
	def get(self, request):
		
		template_name= 'projects.html'

		

		return render(request, template_name )


class DetailProject(View):
	def get(self,request,id_pro):
		template_name = 'detail_project.html'
		##obejto project
		project = get_object_or_404(Project, id = id_pro)

		context = {
			'project':project,
		}

		return render(request, template_name, context)