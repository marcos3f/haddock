from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Incidente(models.Model):
    tipo = models.CharField(max_length=200)

class Criticidade(models.Model):
    nivel = models.IntegerField()
    descricao = models.CharField(max_length=200)

class Areas(models.Model):
    area = models.CharField(max_length=100)
    Coord = models.CharField(max_length=1000)

class UserData(models.Model):
    user = models.CharField(max_length=30)
    grupo = models.CharField(max_length=30)
    area = models.CharField(max_length=30)
    mobile = models.IntegerField()
class Registro(models.Model):
    resolvido = models.CharField(max_length=30)
    criador = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    area = models.CharField(max_length=100)
    localizacao = models.CharField(max_length=300)
    criticidade = models.IntegerField()
    incidente=models.CharField(max_length=300,default='0000000')
    nivel=models.IntegerField(default=0)
