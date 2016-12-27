from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^new/$',
		views.NewProject.as_view(),
		name="new"),
    url(r'^$', views.Projects.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.DetailProject.as_view(), name='detail'),
    ]
