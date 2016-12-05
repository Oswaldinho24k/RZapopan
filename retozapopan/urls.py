from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accountsURLs
from social.apps.django_app import urls as socialURLs
from main import urls as mainUrls
from inputs import urls as inputsURLs
from dashboard import urls as dashboardURLs
from projects import urls as projectsURLs



urlpatterns = [
    url(r'^inputs/',
        include(inputsURLs)),

    url(r'^dashboard/',
        include(dashboardURLs)),

    url(r'^projects/',
        include(projectsURLs)),

    url(r'^accounts/',
        include(accountsURLs)),

    #main
    url(r'^', include(mainUrls)),
    #Social
    url('', include(socialURLs, namespace='social')),
    #Django Admin
    url(r'^admin/', admin.site.urls),

]
