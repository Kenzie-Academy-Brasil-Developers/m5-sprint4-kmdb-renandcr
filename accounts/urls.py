from django.urls import path
from . import views

urlpatterns = [
    path('users/register/', views.CreateUser.as_view()),
    path("users/login/", views.LoginUsers.as_view()),
    path("users/", views.ListAllUsers.as_view()),
    path("users/<int:user_id>/", views.ListUser.as_view()),
]
