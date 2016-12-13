from dajngo import template

register = template.Library()
from projects.models import Project

@register.inclusion_tag('tags/projects/ultimos.html')
def show_latest_posts(count=4):
	latest_projects = Project.object.all().order_by('-publish')[:count]
	return {'latest_projects':latest_projects}