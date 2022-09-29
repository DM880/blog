from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.views import generic as generic_views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from src.data.blog.models import Post, Entry, Image, Comment


def home(request):

    posts = Post.objects.all().order_by("date")[:8]

    return render(request, "home.html", {"posts": posts})


# Sign


def sign(request):

    return render(request, "sign/sign.html")


def sign_in(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        username = request.POST.get("sign_in_username")
        password = request.POST.get("sign_in_password")
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect("home")
        else:
            return render(request, "sign/sign.html", {"error": True})
    else:
        return render(request, "sign/sign.html")


def sign_up(request):

    if request.method == "POST":

        username = request.POST.get("sign_up_username")
        email = request.POST.get("sign_up_email")
        password = request.POST.get("sign_up_password")

        if User.objects.filter(email=email).exists():

            return render(request, "sign/sign.html", {"email_exist": True})

        elif User.objects.filter(username=username).exists():

            return render(request, "sign/sign.html", {"username_exist": True})

        else:
            data_user = {
                "username": email,
                "first_name": username,
                "email": email,
                "password": password,
            }

            User.objects.create_user(**data_user)

            return redirect("home")

    return render(request, "sign/sign.html")


@login_required
def sign_out(request):
    logout(request)
    return redirect("home")


# Blog Sections


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

    if request.user.is_authenticated:
        signed_in = True
    else:
        signed_in = False

    return render(
        request,
        "post.html",
        {
            "post": post,
            "entries": entries,
            "images": images,
            "comments": comments,
            "signed_in": signed_in,
        },
    )


# Comments


@login_required
def create_comment(request, section, post_id):

    post = Post.objects.get(id=post_id)
    section = post.category

    if request.method == "POST":

        comment_post = request.POST.get("comment-post")

        Comment.objects.create(post=post, user=request.user, content=comment_post)

    return redirect(reverse("section_post", args=(section, post_id)))
