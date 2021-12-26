from django.db import models
from django.urls.exceptions import NoReverseMatch

# Create your models here.
class Campo(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao =  models.CharField(max_length=150, verbose_name='Descrição')

    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)

class Atividade(models.Model):
    numero = models.IntegerField(verbose_name='Número')
    descricao = models.CharField(max_length=155, verbose_name='Descrição', null=False, blank=False)
    pontos = models.DecimalField(decimal_places=1, max_digits=3)
    detalhes = models.CharField(max_length=150)
    campo = models.ForeignKey(Campo, on_delete= models.PROTECT)

    #def __str__(self):
    #    return f'{self.numero} {self.descricao} {self.pontos} {self.detalhes}'
    def __str__(self):
        return "{} ({})".format(self.nome, self.descricao)