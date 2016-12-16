from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^$',
		views.Dash.as_view(),
		name="dash"),

	url(r'^(?P<pk>\d+)/$',
		views.Detail.as_view(),
		name="detail"),

	url(r'^(?P<pk>\d+)/basics/$',
		views.Basics.as_view(),
		name="basics"),

	url(r'^(?P<pk>\d+)/history/$',
		views.History.as_view(),
		name="history"),

	url(r'^(?P<pk>\d+)/team/$',
		views.Team.as_view(),
		name="team"),

	url(r'^(?P<pk>\d+)/extra/$',
		views.Extra.as_view(),
		name="extra"),
]