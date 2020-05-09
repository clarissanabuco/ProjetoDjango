from django.contrib import admin
from .models import Dicas


# Register your models here.

class DicasAdmin(admin.ModelAdmin):
   list_display = ('name', 'email', 'fone')


admin.site.register(Dicas, DicasAdmin)





