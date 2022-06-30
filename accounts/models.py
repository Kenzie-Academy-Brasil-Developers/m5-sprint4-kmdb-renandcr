from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import CustomUserManager

class User(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=50, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    objects = CustomUserManager()

    def __repr__(self) -> str:
        return f"model:User - email:{self.email} - id:{self.id}"

