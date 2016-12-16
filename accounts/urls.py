from django.conf.urls import url
from django.contrib.auth.views import logout, login
from . import views


urlpatterns = [
    url(r'^signup/$', views.Registration.as_view(),name="signup"),
	url(r'^profile/$', views.Profiles.as_view(), name="profile"),
	url(r'^login/$', login, name="login"),
	url(r'^logout/$', logout, name="logout"),
]