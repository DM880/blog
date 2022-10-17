from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.views import generic as generic_views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib import messages
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator

import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *

import os


from src.data.blog.models import Post, Entry, Image, Comment
from src.data.newsletter.models import Newsletter


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

        elif User.objects.filter(first_name=username).exists():

            return render(request, "sign/sign.html", {"username_exist": True})

        else:

            data_user = {
                "username": email,
                "first_name": username,
                "email": email,
                "password": password,
            }

            User.objects.create_user(**data_user)

            try:
                Newsletter.objects.get(email=email)
            except Newsletter.DoesNotExist:
                Newsletter.objects.create(name=username, email=email)

            return redirect("home")

    return render(request, "sign/sign.html")


@login_required
def sign_out(request):
    logout(request)
    return redirect("home")


# Delete Account


@login_required
def delete_account(request):
    if request.method == "POST":
        email = request.user.email

        user = User.objects.get(email=email)

        user.delete()

        return redirect("home")


# Account Page


@login_required
def account_page(request):

    if request.user.is_authenticated:

        username = request.user.first_name
        email = request.user.email

        try:
            newsletter = Newsletter.objects.get(email=email)
        except Newsletter.DoesNotExist:
            newsletter = False

    return render(
        request,
        "account_page.html",
        {"username": username, "email": email, "newsletter": newsletter},
    )


@login_required
def newsletter_subscribing(request):
    if request.method == "POST":
        if request.user.is_authenticated:

            email = request.user.email
            newsletter = Newsletter.objects.get(email=email)

            news_in = request.POST.get("newsletter-checkbox")

            if news_in == "checked":
                newsletter.subscribed = True
                newsletter.save()
            else:
                newsletter.subscribed = False
                newsletter.save()

        return redirect("account_page")

    else:
        return redirect("home")


# Search and Sort


def search_and_sort(request):

    section = request.GET.get("category")
    search_input = request.GET.get("search-input")
    sorting_element = request.GET.get("sorting_by")

    if sorting_element is None:
        sorting_element = "-date"

    if section is not None and search_input is not None:
        searched_posts = Post.objects.filter(
            category=section, title__contains=search_input
        ).order_by(sorting_element)

    elif section is None and search_input is not None:
        searched_posts = Post.objects.filter(title__contains=search_input).order_by(
            sorting_element
        )

    elif section is not None and search_input is None:
        searched_posts = Post.objects.filter(category=section).order_by(sorting_element)

    else:
        searched_posts = Post.objects.all().order_by(sorting_element)

    if searched_posts is None:

        searched_posts = []

    return render(
        request,
        "searched_result.html",
        {
            "searched_posts": searched_posts,
            "section": section,
            "search_input": search_input,
        },
    )


# Newsletter


def newsletter_sign_up(request):

    if request.method == "POST":

        name = request.POST.get("name-newsletter")
        email = request.POST.get("email-newsletter")

        if Newsletter.objects.filter(email=email).exists():
            email_exist = "Email is already subscribed"

        else:
            Newsletter.objects.create(name=name, email=email)

        return redirect(request.META.get("HTTP_REFERER"))


def newsletter_sign_up_pop(request):

    if request.method == "POST":

        name = request.POST.get("name-pop-up")
        email = request.POST.get("email-pop-up")

        if Newsletter.objects.filter(email=email).exists():
            email_exist = "Email is already subscribed"

        else:
            Newsletter.objects.create(name=name, email=email)

        return redirect(request.META.get("HTTP_REFERER"))


# Password Reset


def password_reset(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data["email"]
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "password_reset/password_reset_email.txt"
                    c = {
                        "email": user.email,
                        "domain": request.META["HTTP_HOST"],
                        "site_name": "Blog",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": default_token_generator.make_token(user),
                        "protocol": "http",
                    }
                    email = render_to_string(email_template_name, c)
                    message = Mail(
                        from_email=settings.EMAIL_HOST,
                        to_emails=user.email,
                        subject=subject,
                        html_content=email,
                    )

                    try:
                        sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
                        response = sg.send(message)
                        print(response)
                        print(response.status_code)
                    except Exception as e:
                        print(e)

                    messages.success(
                        request,
                        "A message with reset password instructions has been sent to your inbox.",
                    )
                    return redirect("sign")
            else:
                messages.error(request, "An invalid email has been entered.")
                return redirect("sign")

    password_reset_form = PasswordResetForm()
    return render(
        request,
        "password_reset/password_reset.html",
        {"password_reset_form": password_reset_form},
    )


# Blog Sections


def blog_section(request, section):

    posts_section = Post.objects.filter(category=section).order_by("-date")

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
