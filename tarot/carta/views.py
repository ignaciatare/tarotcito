from django.http import HttpResponse
from django.shortcuts import render

from .models import Carta


def index(request):
    tirada = Carta.objects.order_by("?")[:3] 
    return HttpResponse(tirada)

def elCatalogo(request):
    catalogo = Carta.objects.all()
    return render(request, 'templates/pages/catalogo.html', {'catalogo': catalogo})    