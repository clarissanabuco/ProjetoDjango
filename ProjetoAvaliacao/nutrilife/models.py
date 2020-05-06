from django.db import models

# Create your models here.

class Dicas(models.Model):
    name = models.CharField('name', max_length=100)
    email = models.CharField('email', max_length=50)
    fone = models.CharField('fone', max_length=15)



