from django.shortcuts import render
from django.template import loader

from django.http import HttpResponse

from .models import Carta


def miTirada(request):
    tirada = Carta.objects.order_by("?")[:3] 

    return HttpResponse(tirada)