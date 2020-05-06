from django.urls import path
from .views import home, quemsomos, noticias, receberdicas, receitas, contact

urlpatterns = [
   path('', home),
   path('quemsomos', quemsomos),
   path('noticias', noticias),
   path('receberdicas', receberdicas),
   path('receitas', receitas),
   path('contact', contact),
]




