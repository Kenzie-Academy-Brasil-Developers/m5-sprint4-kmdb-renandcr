from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=127)

    def __repr__(self) -> str:
        return f"model:Genre - name:{self.name} - id:{self.id}"
