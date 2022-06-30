from django.urls import path
from . import views 

urlpatterns = [
    path("movies/", views.CreateListAllMovies.as_view()),
    path("movies/<int:movie_id>/", views.ListUpdateDeleteMovie.as_view())
]