from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # path('login/', views.Login.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('signup/', views.signup, name='signup'),
]