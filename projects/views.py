from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from .models import Project

from .forms import NewProjectForm

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.

class NewProject(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name="projects/new.html"
		context = {
			'nav_section':'new'
		}
		return render(request, template_name, context)


	def post(self, request):
		form = NewProjectForm(request.POST)
		if form.is_valid():
			np = form.save(commit=False)
			np.user = request.user
			np.save()
			messages.success(request,"Tu proyecto fué creado con éxito")
			return redirect('dash:dash')
		else:
			messages.error(request,"Algo malo pasó U_U intentalo de nuevo")
			return redirect('projects:new')






class Projects (View):
	def get(self, request):
		
		template_name= 'projects.html'
		projects = Project.objects.all()
		context = {
		'projects':projects
		}

		

		return render(request, template_name, context )


import markdown2
from markdown2 import Markdown


class DetailProject(View):
	def get(self,request,pk):
		template_name = 'projects/detail.html'
		##obejto project
		project = get_object_or_404(Project, id = pk)
		markdowner = Markdown()
		# project.desc = markdown2.markdown(project.desc)
		desc = markdowner.convert(project.desc)

		context = {
			'project':project,
			'desc':desc
		}

		return render(request, template_name, context)