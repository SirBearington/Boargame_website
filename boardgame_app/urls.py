"""Defines URL patterns for boardgame_app."""
from django.urls import path

from . import views

app_name = 'boardgame_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    #Page that shows all topics.
    path('topics/', views.topics, name='topics'), # the 'word/' part tells Django to search for URLs that have the word,after base URL
    # Detail page for a single topic.
    path('topics/<int:topic_id>/',views.topic, name='topic'), # /<int:word_id>/ matches an integer into the // and store the value in word_id
    # when a views funtction is called, the word_id is stored there as an argument
    #Page for adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),

]