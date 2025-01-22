from django.shortcuts import render

def hogar(request):
    return render(request, 'hogar.html')