from django.urls import path
from .views import home, noticias, receitas, contact

urlpatterns = [
   path('', home),
   path('noticias', noticias),
   path('receitas', receitas),
   path('contact', contact),
]