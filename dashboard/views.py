from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from projects.models import Project
from accounts.models import Profile
from .forms import BasicsForm, HistoryForm, ImgForm

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Dash(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "dashboard/perfil.html"
		projects = request.user.projects.all()

		context = {
			'projects':projects
		}
		return render(request, template_name, context)

	def post(self, request):
		try:
			profile = request.user.profile
		except:
			profile = Profile()
			profile.user = request.user
			profile.save()

		form = ImgForm(instance=request.user.profile,data=request.POST, files=request.FILES)
		print(form)
		print(request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, "Tu Perfil se actualizó con exito")
		else:
			messages.error(request, "Algo malo pasó, U_U intenta de nuevo")
		return redirect('dash:dash')

class Detail(View):
	def get(self, request, pk):
		template_name = "dashboard/dash.html"
		p = get_object_or_404(Project, id=pk)
		context = {
			'project':p,
			'section':'dash'
		}
		return render(request, template_name,context)

class Basics(View):
	def get(self, request, pk):
		template_name = "dashboard/basics.html"
		p = get_object_or_404(Project, id=pk)
		form = BasicsForm()
		context = {
			'project':p,
			'section':'basics',
			'form':form
		}
		return render(request, template_name,context)

	def post(self, request, pk):
		template_name = "dashboard/basics.html"
		p = get_object_or_404(Project, id=pk)
		if p.publish:
			messages.error(request, "Tu proyecto ya se publicó, no puedes modificarlo")
			return redirect('dash:basics',pk=pk)
		data = request.POST.dict()
		form = BasicsForm(data,request.FILES,instance=p)
		# print(form)

		if form.is_valid():
			form.save()
			print('PASO Y GUARDO')
			messages.success(request, "Proyecto guardado con éxito")
		else:
			print('No es Valido')

			messages.error(request, "El proyecto no se guardó")


		context = {
			'project':p,
			'section':'basics',
		}
		return render(request, template_name,context)


class History(View):
	def get(self, request, pk):
		template_name = "dashboard/history.html"
		p = get_object_or_404(Project, id=pk)
		context = {
			'project':p,
			'section':'history'
		}
		return render(request, template_name,context)

	def post(self, request, pk):
		template_name = "dashboard/history.html"
		p = get_object_or_404(Project, id=pk)
		data = request.POST.dict()
		form = HistoryForm(data,instance=p)
		print(form)
		# print(form)

		if form.is_valid():
			form.save()
			print('PASO Y GUARDO')
			messages.success(request, "Proyecto guardado con éxito")
		else:
			print('No es Valido')
			messages.error(request, "El proyecto no se guardó")

		context = {
			'project':p,
			'section':'history',
		}
		return render(request, template_name,context)



class Team(View):
	def get(self, request, pk):
		template_name = "dashboard/basics.html"
		p = get_object_or_404(Project, id=pk)
		context = {
			'project':p,
			'section':'team'
		}
		return render(request, template_name,context)

class Extra(View):
	def get(self, request, pk):
		template_name = "dashboard/basics.html"
		p = get_object_or_404(Project, id=pk)
		context = {
			'project':p,
			'section':'extra'
		}
		return render(request, template_name,context)




# Panels del lado del que apoya incluyendo chat

class Support(View):
	def get(self, request):
		template_name = "dashboard/founder.html"
		p = request.user.funds.all()
		context = {
			'projects':p
		}
		return render(request, template_name, context)

class Chating(View):
	def get(self, request, pk):
		template_name = "dashboard/founder.html"
		project = get_object_or_404(Project,id=pk)
		p = request.user.funds.all()
		print(request.user.cchats.all())
		chat = request.user.cchats.all().get(project=project)
		
		context = {
			'projects':p,
			'chat':chat
		}
		return render(request, template_name, context)

