from django.contrib import admin
from .models import Product
from .models import Dicas
from .models import Categoria
from .models import Estilo

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
   list_display = ('tipo', 'categoria')


admin.site.register(Categoria, CategoriaAdmin)


class EstiloAdmin(admin.ModelAdmin):
   list_display = ('codigo', 'estilo')


admin.site.register(Estilo, EstiloAdmin)


class ProductAdmin(admin.ModelAdmin):
  list_display = ('name', 'price', 'stock')


admin.site.register(Product, ProductAdmin)


class DicasAdmin(admin.ModelAdmin):
   list_display = ('name', 'email', 'fone')


admin.site.register(Dicas, DicasAdmin)



