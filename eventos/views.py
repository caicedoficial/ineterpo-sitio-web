from django.shortcuts import render
from .models import Eventos

def eventos(request):
    eventos = Eventos.objects.all()[:7]

    return render(request, 'eventos.html', {'eventos': eventos})