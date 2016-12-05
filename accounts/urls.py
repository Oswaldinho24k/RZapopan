from django.conf.urls import url
from django.contrib.auth import views as djangoViews


urlpatterns = [
    url(r'^login',
        djangoViews.login,
        name="login"),

    url(r'^logout',
            djangoViews.logout,
            name="logout"),
]