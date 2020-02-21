# internships/urls.py

from django.urls import path

from .views import InternshipsListView

urlpatterns = [
    path('', InternshipsListView.as_view(), name='internships'),
]
