from django.urls import path
from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.show, name="Show"),
    path("wiki/<str:Title>", views.show, name="show")
]
