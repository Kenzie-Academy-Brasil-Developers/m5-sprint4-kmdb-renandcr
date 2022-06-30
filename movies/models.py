from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10)
    premiere = models.DateField()
    classification = models.IntegerField()
    synopsis = models.TextField()

    genres = models.ManyToManyField("genres.Genre", related_name="movies")

    def __repr__(self) -> str:
        return f"model:Movie - title:{self.title} - id:{self.id}"

