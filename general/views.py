from django.shortcuts import render
from .models import Institucional, Eventos, Implementaciones

def institucional(request):
    institucional = Institucional.objects.all()[:10]

    return render(request, 'general.html', {'objetos': institucional})

def eventos(request):
    eventos = Eventos.objects.all()[:10]

    return render(request, 'general.html', {'objetos': eventos})

def implementaciones(request):
    implementaciones = Implementaciones.objects.all()[:10]

    return render(request, 'general.html', {'objetos': implementaciones})