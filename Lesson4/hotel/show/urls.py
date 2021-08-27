from django.urls import path
from . import views

app_name ="show"

urlpatterns = [
    path("", views.index,name= "index"),
    path("available/", views.available, name="available"),
    path("booked", views.booked, name="booked")
]