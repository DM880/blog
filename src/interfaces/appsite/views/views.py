from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.views import generic as generic_views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from src.data.blog.models import Post, Entry, Image, Comment


def home(request):
    return render(request, "home.html")


def travel(request):

    travel_posts = Post.objects.filter(category='TRAVEL').order_by("date")

    return render(request, "sections/travel.html", {"travel_posts": travel_posts})


def travel_post(request, post_id):

    post = Post.objects.get(id=post_id)
    entries = Entry.objects.filter(post=post)
    images = Image.objects.filter(post=post)
    comments = Comment.objects.filter(post=post)

    return render(
        request,
        "post.html",
        {"post": post, "entries": entries, "images": images, "comments": comments},
    )
