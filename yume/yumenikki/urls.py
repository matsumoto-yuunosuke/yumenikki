from django.urls import path
from .views import *
from . import views

urlpatterns = [
  path('', views.dream_list_view, name='dream_list'),
  path('dream_detail/<int:pk>/', views.dream_detali_view, name='dream_detail'),
  path('dream_update/<int:pk>/', views.DreamUpdate.as_view(), name='dream_update'),
  path('dream_delete/<int:pk>/', views.DreamDelete.as_view(), name='dream_delete'),
  path('dream_create/', views.dream_upload, name='dream_create'),
  path('idea_list/', views.IdeaList.as_view(), name='idea_list'),
  # path('dream_idea_detail/<int:pk>/', views.DreamIdeaDetail.as_view(), name='dream_idea_detail'),
  path('idea_detail/<int:pk>/', views.idea_detali_view, name='idea_detail'),
  path('idea_create/<int:pk>/', views.idea_upload, name='idea_create'),
  path('idea_delete/<int:pk>/', views.IdeaDelete.as_view(), name='idea_delete'),
  path('tags/<slug:slug>/', views.tags, name='tags'),
  # path('calendar/<int:pk>/<int:year>/<int:month>', views.CalendarView.as_view(), name='calendar'),
]
