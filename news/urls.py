from os import name
from django.urls import path

from news.models import Articolo,Giornalista
from .views import *

app_name="news"

urlpatterns = [
    path('', home, name="homeview"),
    #path("articoli/<int:pk>", articoloDetailView, name="articolo_detail")
    path("articoli/<int:pk>", ArticoloDetailViewCB.as_view(), name="articolo_detail"),
    path("lista_articoli/",ArticoloListView.as_view(), name="lista_articoli"),
    path("giornalisti/<int:pk>", GiornalistaDetailViewCB.as_view(), name="giornalisti_detail"),
    path("lista_giornalisti/",GiornalistaListView.as_view(), name="lista_giornalisti"),
]
