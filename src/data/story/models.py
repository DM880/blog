from django.db import models
from django.contrib.auth.models import User
import datetime


CATEGORY_CHOICES = (
    (TRA := "TRAVEL", "travel"),
    (BOK := "BOOK", "book"),
    (OTH := "OTHER", "other"),
)


class Post(models.Model):
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=OTH)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)
    view = models.IntegerField()


class Entry(models.Model):
    class Meta:
        verbose_name_plural = "entries"

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    title = models.CharField(max_length=100)
    content = models.TextField()


class Image(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to="post/")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
