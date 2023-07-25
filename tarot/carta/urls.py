from django.urls import path
from . import views

urlpatterns = [
    path('tirada/', views.laTirada, name='mi_tirada'),
    path('catalogo/', views.elCatalogo, name='las_cartas'),

]
