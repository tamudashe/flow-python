# algotutor/views.py

from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import TemplateView  # new
from .models import Post

# Create your views here.
class AlgotutorPageView(TemplateView):
    template_name = 'algotutor.html'