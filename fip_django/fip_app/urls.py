from django.urls import path
from . import views

urlpatterns = [
    path('', views.filter_psychologists, name='filter_psychologists'),
]
