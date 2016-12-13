from django import template

register = template.Library()
from projects.models import Project

@register.inclusion_tag('tags/ultimos.html')
def show_latest_posts(count=4):
	latest_projects = Project.objects.all().order_by('-publish')[:count]
	return {'latest_projects':latest_projects}

@register.simple_tag
def count_projects():
	return Project.objects.all().count()