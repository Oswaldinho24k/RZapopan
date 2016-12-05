from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accountsURLs
from social.apps.django_app import urls as socialURLs
from main import urls as mainUrls



urlpatterns = [
    url(r'^accounts/',
        include(accountsURLs)),
    url(r'^admin/', admin.site.urls),
    #Social
    url('', include(socialURLs, namespace='social')),
    #main
    url(r'^', include(mainUrls)),

]
