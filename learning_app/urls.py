""" Defines URL patterns for learning_app."""
from django.urls import path
from . import views

# Use app_name to replace namespace
app_name = 'learning_app'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]