from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accountsURLs
from social.apps.django_app import urls as socialURLs
from main import urls as mainUrls
from inputs import urls as inputsURLs
from dashboard import urls as dashboardURLs
from projects import urls as projectsURLs



urlpatterns = [

    #main
    url(r'^', include(mainUrls)),
    
    url(r'^inputs/',
        include(inputsURLs)),

    url(r'^dashboard/',
        include(dashboardURLs, namespace="dash")),

    url(r'^projects/',
        include(projectsURLs)),

    url(r'^accounts/',
        include(accountsURLs)),

    
    #Social
    url('', include(socialURLs, namespace='social')),
    #Django Admin
    url(r'^admin/', admin.site.urls),

]
