from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')

def noticias(request):
    return render(request, 'noticias.html')

def receitas(request):
    return render(request, 'receitas.html')

def contact(request):
    return render(request, 'contact.html')
