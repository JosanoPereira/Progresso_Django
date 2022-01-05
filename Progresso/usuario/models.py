from django.db import models
from django.contrib.auth.models import User
<<<<<<< Updated upstream


=======
>>>>>>> Stashed changes
# Create your models here.

class Perfil(models.Model):
    nome_completo = models.CharField(max_length=50, null=True)
<<<<<<< Updated upstream
    bi = models.CharField(max_length=14, null=True, verbose_name='BI')
    telefone = models.CharField(max_length=16, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
=======
    bi = models.CharField(max_length=14, null=True)
    telefone = models.CharField(max_length=13, null=True)
    #usuario = models.OneToOneField(User, on_delete=models.PROTECT(collector=True, field=True, sub_objs=User, using=True))

>>>>>>> Stashed changes
