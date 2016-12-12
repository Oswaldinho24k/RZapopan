from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^$',
		views.Dash.as_view(),
		name="dash"),
]