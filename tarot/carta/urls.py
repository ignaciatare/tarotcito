from django.urls import path
from . import views

urlpatterns = [
    path("tirada/", views.tirada3, name="tirada"),

    path("catalogo/", views.elCatalogo, name='catalogo'),
]
