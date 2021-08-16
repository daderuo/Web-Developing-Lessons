from  django.urls import  path

from . import views


#vale l'ordine in cui scrivo le casistiche: i casi generici vanno in fondo, quelli specifici all'inizio
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.hitoyou, name="hitoyou") ,
    path("davide", views.davide, name="davide")       
]