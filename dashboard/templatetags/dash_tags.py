from django import template

register = template.Library()
from projects.models import Project

# from django.core import serializers
import json


@register.inclusion_tag('tags/ultimos.html')
def show_latest_posts(count=4):
    latest_projects = Project.objects.all().order_by('-publish')[:count]
    return {'latest_projects': latest_projects}


@register.simple_tag
def count_projects():
    return Project.objects.all().count()


# Tests David

@register.inclusion_tag('tags/projects_permonth.html')
def graphics_projects_permonth():
    arr = []
    def range_dates():
        for number in range(1, 13):
            projects_permonth = Project.objects.all().filter(publish__year=2016, publish__month=number).count()
            arr.append(projects_permonth)

        return arr

    return {
        'projects_permonth':range_dates()
    }


@register.inclusion_tag('tags/grafica_metas.html')
def graphics_goals():
    project_goals_under_50k_count = Project.objects.all().filter(goal__gt=0, goal__lt=50000).count()
    project_goals_btw_50k_300k_count = Project.objects.all().filter(goal__gt=50001, goal__lt=300000).count()
    project_goals_over_300k_count = Project.objects.all().filter(goal__gt=300001).count()

    return {
        'project_goals_under_50k_count': project_goals_under_50k_count,
        'project_goals_btw_50k_300k_count': project_goals_btw_50k_300k_count,
        'project_goals_over_300k_count': project_goals_over_300k_count
    }


'''Django View

django_list = list(Some_Object.objects.all())
json_list = simplejson.dumps(django_list)
Template HTML + JS

<script type="text/javascript" >
    var js_list = {{json_list}};
</script>'''
