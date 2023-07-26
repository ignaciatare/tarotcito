from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="tirada"),

    path('catalogo/', views.elCatalogo, name='catalogo'),

]
