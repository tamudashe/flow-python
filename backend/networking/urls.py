# networking/urls.py

from django.urls import path

from .views import NetworkingListView

urlpatterns = [
    path('', NetworkingListView.as_view(), name='networking'),
]
