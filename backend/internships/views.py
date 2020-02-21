# internships/views.py

from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class InternshipsListView(ListView):
    model = Post
    template_name = 'internships.html'