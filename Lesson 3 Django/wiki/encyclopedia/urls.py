from django.urls import path
from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/", views.show, name="Show"),
    path("wiki/editor/", views.new, name="new"),    
    path("wiki/rand", views.Rand, name="random"),
    path("wiki/editor/<str:Title>", views.edit, name="edit"),
    path("wiki/<str:Title>", views.show, name="show")
]
