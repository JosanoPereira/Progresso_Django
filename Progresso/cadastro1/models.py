from enum import Flag
from django.db import models

# Create your models here.

class Campo(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao =  models.CharField(max_length=150, verbose_name='Descrição')

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name='Número', unique=True)
    descricao = models.CharField(max_length=155, verbose_name='Descrição', null=False, blank=False)
    pontos = models.DecimalField(decimal_places=1, max_digits=3)
    detalhes = models.CharField(max_length=150, null=True, blank=True)
    campo = models.ForeignKey(Campo, on_delete= models.PROTECT)

    def __str__(self):
        return "{} - {} ({})".format(self.numero, self.descricao, self.campo)

class Status(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=150)
    
    def __str__(self):
        return "{} - {}".format(self.nome, self.descricao)

class Campus(models.Model):
    cidade = models.CharField(max_length=100)
    endereco = models.CharField(max_length=70, verbose_name='Endereço')
    telefone = models.CharField(max_length=14, null=False, blank=False)
    
    def __str__(self):
        return "{} - {}".format(self.cidade, self.endereco)

class Classe(models.Model):
    nome = models.CharField(max_length=100)
    nivel = models.IntegerField(verbose_name='Nível')
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return "{} - {}".format(self.nome, self.descricao)
