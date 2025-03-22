from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('games/had/', views.had, name='had'),
]