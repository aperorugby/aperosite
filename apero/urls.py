from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^$', 'apero.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apero.home.urls')),
    url(r'^aperomembres/', include('apero.membersection.urls',
                                   namespace='aperomembre')),

)
