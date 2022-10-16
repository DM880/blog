from django.db import models
from django.contrib.auth.models import User


class Newsletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}/{self.email}"
