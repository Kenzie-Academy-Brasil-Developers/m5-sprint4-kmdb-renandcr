from django.urls import path
from . import views

urlpatterns = [
    path("movies/<int:movie_id>/reviews/", views.CreateListAllMovieReview.as_view()),
    path("reviews/<int:review_id>/", views.DeleteReview.as_view()),
    path("reviews/", views.ListAllReviews.as_view()),
]
