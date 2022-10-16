from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


from .views import views

urlpatterns = [
    path("", views.home, name="home"),
    # Search and Sort
    path("search_and_sort/", views.search_and_sort, name="search_and_sort"),
    # Sign
    path("sign/", views.sign, name="sign"),
    path("sign/sign_in/", views.sign_in, name="sign_in"),
    path("sign/sign_up/", views.sign_up, name="sign_up"),
    path("sign/sign_out/", views.sign_out, name="sign_out"),
    # Account Page
    path("account_page/", views.account_page, name="account_page"),
    # Newsletter
    path("newsletter_sign_up/", views.newsletter_sign_up, name="newsletter_sign_up"),
    path(
        "newsletter_sign_up_pop/",
        views.newsletter_sign_up_pop,
        name="newsletter_sign_up_pop",
    ),
    # Password Reset
    path("password_reset/", views.password_reset, name="password_reset"),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    # Blog Sections
    path("<section>/", views.blog_section, name="blog_section"),
    path("<section>/<post_id>/", views.section_post, name="section_post"),
    # Comments
    path(
        "<section>/<post_id>/create_comment/",
        views.create_comment,
        name="create_comment",
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
