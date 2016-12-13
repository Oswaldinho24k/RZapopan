from django.conf.urls import url
from . import views
from django.contrib.auth import views as djangoViews


urlpatterns = [
    url(r'^login',
        djangoViews.login,
        name="login"),

    url(r'^logout',
            djangoViews.logout,
            name="logout"),
    url(r'^profile', views.Profile.as_view(), name="profile"),
    url(r'^signup', views.Registration.as_view(), name="signup"),
]