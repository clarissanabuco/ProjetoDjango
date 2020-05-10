from django.urls import path
from .views import home, quemsomos, noticias, receitas, contact, ListCateg, listestilo, listprodutos, listclientes, listagens

urlpatterns = [
  path('',home),
  path('quemsomos', quemsomos),
  path('noticias', noticias),
  path('receitas', receitas),
  path('contact', contact),
  path('ListCateg', ListCateg),
  path('listestilo', listestilo),
  path('listprodutos', listprodutos),
  path('listclientes', listclientes),
  path('listagens', listagens),
]
