from django.shortcuts import render
from .models import Noticias

def noticias(request):
    noticias = Noticias.objects.all()

    return render(request, 'noticias.html', {'noticias': noticias})