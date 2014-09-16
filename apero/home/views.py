from django.views.generic import TemplateView
from .mixins import ActiveTabMixin

class HomeView(ActiveTabMixin, TemplateView):

    template_name = "home.html"
    active_tab = "home"

