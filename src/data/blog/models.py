from django.db import models
from django.contrib.auth.models import User
import datetime


CATEGORY_CHOICES = (
    (TRA := "TRAVEL", "travel"),
    (BOK := "BOOK", "book"),
    (OTH := "OTHER", "other"),
)


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default=OTH)
    date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)
    views = models.IntegerField(default=0)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"


class Entry(models.Model):
    class Meta:
        verbose_name_plural = "entries"

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="entry")
    title = models.CharField(max_length=100)
    content = models.TextField()
    visible = models.BooleanField(default=True)


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="image")
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="entry")
    image = models.ImageField(upload_to="post/")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
