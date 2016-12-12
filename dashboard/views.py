from django.shortcuts import render
from django.views.generic import View


class Dash(View):
	def get(self, request):
		template_name = "dashboard/dash.html"
		return render(request, template_name)
