from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    """
    Modelo do usuário padrão do sistema
    """
    tipo = models.CharField(max_length=1)
    email_1 = models.CharField(max_length=255)
    email_2 = models.CharField(max_length=255)
    telefone_1 = models.CharField(max_length=255)
    telefone_2 = models.CharField(max_length=255)

class Candidato(models.Model):
    """
    Modelo do usuário candidato
    """
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)

class Empresa(models.Model):
    """
    Modelo do usuário empresa
    """
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)