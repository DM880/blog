from django.urls import path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


from .views import views

urlpatterns = [
    path("", views.home, name="home"),
    path("travel/", views.travel, name="travel"),
    path("travel/<post_id>/", views.travel_post, name="travel_post"),
]
