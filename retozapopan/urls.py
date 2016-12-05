from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accountsURLs
from social.apps.django_app import urls as socialURLs

urlpatterns = [
    url(r'^accounts/',
        include(accountsURLs)),
    url(r'^admin/', admin.site.urls),
    #Social
    url('', include(socialURLs, namespace='social'))
]
