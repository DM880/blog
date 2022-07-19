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
    title = models.TextField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    date = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now)
    view = models.IntegerField()


class Entry(models.Model):
    name = models.TextField(max_length=100)
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post")


class Image(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, related_name="image")
    image = models.ImageField(upload_to="post/")


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)