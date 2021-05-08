from django.urls import path
from .views import *
from . import views

urlpatterns = [
  path('dream_list/', views.DreamList.as_view(), name='dream_list'),
  path('dream_detail/<int:pk>/', views.DreamDetail.as_view(), name='dream_detail'),
  path('dream_idea_detail/<int:pk>/', views.DreamIdeaDetail.as_view(), name='dream_idea_detail'),
  path('dream_update/<int:pk>/', views.DreamUpdate.as_view(), name='dream_update'),
  path('dream_delete/<int:pk>/', views.DreamDelete.as_view(), name='dream_delete'),
  path('dream_create/', views.dream_upload, name='dream_create'),
  path('idea_list/', views.IdeaList.as_view(), name='idea_list'),
  path('idea_detail/<int:pk>/', views.IdeaDetail.as_view(), name='idea_detail'),
  path('idea_create/', views.idea_upload, name='idea_create'),
]
