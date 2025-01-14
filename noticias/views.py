from django.shortcuts import render
from .models import Noticias

def noticias(request):
    noticias = Noticias.objects.all().order_by('-fecha')[:7]

    return render(request, 'noticias.html', {'noticias': noticias})