"""Defines URL patterns for boardgame_app."""
from django.urls import path

from . import views

app_name = 'boardgame_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    #Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    
]