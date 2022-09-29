from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


from .views import views

urlpatterns = [
    path("", views.home, name="home"),
    # Sign
    path("sign/", views.sign, name="sign"),
    path("sign/sign_in/", views.sign_in, name="sign_in"),
    path("sign/sign_up/", views.sign_up, name="sign_up"),
    path("sign/sign_out/", views.sign_out, name="sign_out"),
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
