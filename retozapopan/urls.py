from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as accountsURLs
from social.apps.django_app import urls as socialURLs
from main import urls as mainUrls
from inputs import urls as inputsURLs
from dashboard import urls as dashboardURLs
from projects import urls as projectsURLs
from cart import urls as cartURLs

from django.views.static import serve
from django.conf import settings


urlpatterns = [

    # Social Auth
    url('',
        include(socialURLs,
            namespace="social")),
    #main
    url(r'^', include(mainUrls)),

    url(r'^inputs/',
        include(inputsURLs)),

    url(r'^dashboard/',
        include(dashboardURLs, namespace="dash")),

    url(r'^projects/',
        include(projectsURLs, namespace="projects")),

    url(r'^accounts/',
        include(accountsURLs)),

    url(r'^cart/',
        include(cartURLs, namespace="cart")),

    #Django Admin
    url(r'^admin/', admin.site.urls),

    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}
        ),

]
