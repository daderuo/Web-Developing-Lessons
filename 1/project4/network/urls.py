
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("posts", views.posts, name="posts"),
    path("profile/<str:user>", views.profile, name="profile"),
    path("follow", views.follow, name="follow"),
    path("add_follow", views.add_follow, name="add_follow"),
    path("remove_follow", views.remove_follow, name="remove_follow"),
    path("p_f", views.index, name="p_f"),
    path("update", views.update, name="update"),
]
