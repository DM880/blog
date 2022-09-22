from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.views import generic as generic_views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from src.data.blog.models import Post, Entry, Image, Comment


def home(request):

    posts = Post.objects.all().order_by("date")[:8]

    return render(request, "home.html", {"posts": posts})


def blog_section(request, section):

    posts_section = Post.objects.filter(category=section).order_by("date")

    return render(
        request, "sections.html", {"posts_section": posts_section, "section": section}
    )


def section_post(request, section, post_id):

    post = Post.objects.get(id=post_id)
    entries = Entry.objects.filter(post=post)
    images = Image.objects.filter(post=post)
    comments = Comment.objects.filter(post=post)

    return render(
        request,
        "post.html",
        {"post": post, "entries": entries, "images": images, "comments": comments},
    )


def create_comment(request, section, post_id):

    post = Post.objects.get(id=post_id)
    section = post.category

    if request.method == "POST":

        comment_post = request.POST.get('comment-post')

        Comment.objects.create(post=post, user=request.user, content=comment_post)


    return redirect(reverse('section_post', args=(section,post_id)))