# internships/views.py

from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class NetworkingListView(ListView):
    model = Post
    template_name = 'networking.html'