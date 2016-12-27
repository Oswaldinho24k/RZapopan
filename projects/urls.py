from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new/$',
		views.NewProject.as_view(),
		name="new"),
    url(r'^$', views.Projects.as_view(), name='projects'),
    url(r'^detail_project/(?P<id_pro>\d+)/$', views.DetailProject.as_view(), name='detail_project'),
    ]
