from django.conf.urls import patterns, include, url

urlpatterns = patterns('apero.old.views',
    url(r'^$', 'home', name='old_home'),
)
