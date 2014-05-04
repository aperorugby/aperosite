from django.shortcuts import render

def home(request):
    """Page d'accueil"""
    c = {
    }
    return render(request, "home.html", c)
