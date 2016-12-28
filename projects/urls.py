from django.conf.urls import url
from . import views

urlpatterns = [
	
	url(r'^json/(?P<pk>\d+)/$',
		views.JsonRewards.as_view(),
		name="json_rewards"),

	url(r'^explorar/(?P<cat>[-\w]+)/$',
		views.Explorar.as_view(),
		name="categoria"),

	url(r'^explorar/$',
		views.Explorar.as_view(),
		name="explorar"),

	url(r'^new/$',
		views.NewProject.as_view(),
		name="new"),
    url(r'^$', views.Projects.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.DetailProject.as_view(), name='detail'),
    ]
