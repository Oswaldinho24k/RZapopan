from django import template

register = template.Library()
from projects.models import Project

# from django.core import serializers
import json


@register.inclusion_tag('tags/ultimos.html')
def show_latest_posts(count=4):

	latest_projects = Project.objects.all().order_by('-publish')[:count]

	context = {
	'latest_projects':latest_projects,
	}
	return context

@register.simple_tag
def count_projects():
	return {
	're':"8,000.00",
	'pe':"12,000.00"
	}

    #latest_projects = Project.objects.all().order_by('-publish')[:count]
    #return {'latest_projects': latest_projects}


@register.simple_tag
def count_projects():
    return Project.objects.all().count()


# Tests David

@register.inclusion_tag('tags/grafica_metas.html')
def graphics_goals():

    project_goals_under_50k = list(Project.objects.all().filter(goal__gt=0, goal__lt=50000))
    project_goals_btw_50k_300k = list(Project.objects.all().filter(goal__gt=50001, goal__lt=300000))
    project_goals_over_300k = list(Project.objects.all().filter(goal__gt=300001))
    project_goals_under_50k_count = Project.objects.all().filter(goal__gt=0, goal__lt=50000).count()
    project_goals_btw_50k_300k_count = Project.objects.all().filter(goal__gt=50001, goal__lt=300000).count()
    project_goals_over_300k_count = Project.objects.all().filter(goal__gt=300001).count()

    goals_under_50k = []
    goals_btw_50k_300k = []
    goals_over_300k = []

    def create_arr(arr,data):
        for project in data:
            number = int(project.goal)
            arr.append(number)
        return arr

    return {
        'project_goals_under_50k': create_arr(goals_under_50k,project_goals_under_50k),
        'project_goals_btw_50k_300k': create_arr(goals_btw_50k_300k,project_goals_btw_50k_300k),
        'project_goals_over_300k': create_arr(goals_over_300k,project_goals_over_300k),
        'project_goals_under_50k_count':project_goals_under_50k_count,
        'project_goals_btw_50k_300k_count':project_goals_btw_50k_300k_count,
        'project_goals_over_300k_count':project_goals_over_300k_count
    }


'''Django View

django_list = list(Some_Object.objects.all())
json_list = simplejson.dumps(django_list)
Template HTML + JS

<script type="text/javascript" >
    var js_list = {{json_list}};
</script>'''

