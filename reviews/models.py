from django.db import models

class RecomendationReview(models.TextChoices):
    MUST_WATCH = ("Must Watch")
    SHOULD_WATCH = ("Should Watch")
    AVOID_WATCH = ("Avoid Watch")
    NO_Opinion = ("No Opinion")

class Review(models.Model):
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(
        max_length=50,
        choices=RecomendationReview.choices,
        default=RecomendationReview.NO_Opinion,
    )

    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name="reviews")

    def __repr__(self) -> str:
        return f"model:Review - id:{self.id} - movie_id:{self.movie_id} - user_id:{self.user_id}"