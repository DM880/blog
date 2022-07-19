from django.db import models
from django.contrib.auth.models import User
import datetime


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name =  models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)
    view = models.IntegerField()


class Entry(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")
    title = models.TextField(max_length=100)
    content = models.TextField()


class Image(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to="post/")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)