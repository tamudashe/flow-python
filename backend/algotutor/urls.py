# algotutor/urls.py

from django.urls import path

from .views import AlgotutorPageView

urlpatterns = [
    path('', AlgotutorPageView.as_view(), name='algotutor'),
]
