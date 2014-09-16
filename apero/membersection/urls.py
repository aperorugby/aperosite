from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('^$',
                       url(r'',
                           views.LoginView.as_view(),
                           name='login'),
                       url(r'password-reset',
                           views.PasswordResetView.as_view(),
                           name='password-reset'),
                      )
