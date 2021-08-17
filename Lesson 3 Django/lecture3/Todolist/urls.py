from  django.urls import  path

from . import views

app_name = "task"
#vale l'ordine in cui scrivo le casistiche: i casi generici vanno in fondo, quelli specifici all'inizio
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("remove/", views.remove, name="remove"),
]