from django.shortcuts import render
from nutrilife.models import Categoria
from nutrilife.models import Estilo
from nutrilife.models import Product
from nutrilife.models import Dicas

# Create your views here.

def home(request):
   return render(request, 'home.html')

def quemsomos(request):
    return render(request, 'quemsomos.html')

def noticias(request):
    return render(request, 'noticias.html')

def receitas(request):
    return render(request, 'receitas.html')

def contact(request):
    return render(request, 'contact.html')

def ListCateg(request):
    listadecategorias = Categoria.objects.all()
    contex = {
        'categorias': listadecategorias
    }
    return render(request, 'ListCateg.html', contex)

def listestilo(request):
    listadeestilos = Estilo.objects.all()
    contex = {
        'estilos':listadeestilos
    }
    return  render(request, 'listestilo.html', contex)

def listprodutos(request):
    listprodutos = Product.objects.all()
    contex = {
        'produtos':listprodutos
    }
    return render(request, 'listprodutos.html', contex)

def listclientes(request):
    listclientes = Dicas.objects.all()
    context = {
        'clientes':listclientes
    }
    return render(request, 'listclientes.html', context)

def listagens(request):
    return render(request, 'listagens.html')