from django.urls import path
from . import views

urlpatterns = [
    path('tirada/', views.miTirada, name='mi_tirada'),
]
