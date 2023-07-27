from django.http import HttpResponse
from django.shortcuts import render

from .models import Carta


def tirada3(request):
    tirada = Carta.objects.order_by("?")[:3] 
    context = {'cartas': tirada}
    return render(request, 'pages/tirada.html', context)

def elCatalogo(request):
    cartas = Carta.objects.all()
    context = {'cartas': cartas}
    return render(request, 'pages/catalogo.html', context)
