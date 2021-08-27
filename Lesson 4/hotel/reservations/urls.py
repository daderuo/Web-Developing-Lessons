from django.urls import path
from . import views

app_name = "reservations"

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add_guest, name="add_guest" ),
    path("guest/<int:guest_id>", views.guest, name="guest")
]


