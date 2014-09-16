from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from apero.home.mixins import ActiveTabMixin


class LoginView(ActiveTabMixin, FormView):

    active_tab = 'login'
    template_name = 'membersection/login.html'
    form_class = AuthenticationForm

class PasswordResetView(ActiveTabMixin, FormView):

    active_tab = 'login'
    template_name = 'membersection/login.html'
    form_class = AuthenticationForm
