from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Project.as_view(), name='preject'),
    ]
