from django.db import models

# Create your models here
# .

class Categoria(models.Model):
# se Alimento ou Bebida / Beleza e Bem Estar / Emagrecimento / Esporte / Vitaminas
    tipo = models.IntegerField('tipo')
    categoria = models.CharField('categoria', max_length=50)


class Estilo(models.Model):
# se Vegetariano / Vegano / Sem Açucar / Sem Gluten / Low Carb
    codigo = models.IntegerField('codigo')
    estilo = models.CharField('estilo', max_length=50)


class Product(models.Model):
    name = models.CharField('name', max_length=100)
    price = models.DecimalField('price', decimal_places=2, max_digits=6)
    stock = models.IntegerField('amount')

class Dicas(models.Model):
    name  = models.CharField('name', max_length=100)
    email = models.CharField('email', max_length=50)
    fone  = models.CharField('fone', max_length=15)



