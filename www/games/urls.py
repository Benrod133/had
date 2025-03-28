from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='start'),
    path('games', views.games, name='index'),
    path('games/had/', views.had, name='had'),
    path('error/', views.error, name='error'),
]