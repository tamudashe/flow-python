# landing/views.py

from django.shortcuts import render
from django.views.generic import TemplateView  # new

# Create your views here.
class LandingPageView(TemplateView):
    template_name = 'home.html'
