from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import View
from django.views.generic import ListView

from .models import Project, Reward

from .forms import NewProjectForm

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.core import serializers

from taggit.models import Tag



class Explorar(ListView):
	template_name = "projects/explorar.html"
	# queryset = Project.objects.all()
	context_object_name = 'projects'
	paginate_by = 1
	

	def get_queryset(self):
		try:
			tag = get_object_or_404(Tag, slug=self.kwargs['cat'])
			return Project.objects.all().filter(tags__in=[tag])
		except:
			return Project.objects.all()


	def get_context_data(self, **kwargs):
		context = super(Explorar, self).get_context_data(**kwargs)
		context['nav_section'] = "explorar"
		try:
			tag = get_object_or_404(Tag, slug=self.kwargs['cat'])
			context['categoria'] = tag
		except:
			pass
		return context



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
		project.desc = markdowner.convert(project.desc)

		context = {
			'project':project,
		}

		return render(request, template_name, context)


class JsonRewards(View):
	def get(self, request, pk):
		r = get_object_or_404(Reward, id=pk)
		data = serializers.serialize('json',[r],indent=2,
			use_natural_foreign_keys=False, use_natural_primary_keys=False)
		return HttpResponse(data,content_type = 'application/javascript; charset=utf8') 








