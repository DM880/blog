from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


from .views import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<section>/", views.blog_section, name="blog_section"),
    path("<section>/<post_id>/", views.section_post, name="section_post"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
