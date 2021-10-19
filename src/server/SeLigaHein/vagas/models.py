from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class Usuario(AbstractUser):
    """
    Modelo do usuário padrão do sistema
    """
    email_2 = models.CharField(max_length=255, null=True, blank=True)#o django já possui um campo de email
    telefone_1 = models.CharField(max_length=255, null=True, blank=True)
    telefone_2 = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)#campo de bio ou descrição de uma empresa

    def nome_completo(self):
        """
        Retorna o nome completo do usuário
        """
        return "{0} {1}".format(self.first_name, self.last_name)

    def __str__(self):
        return "Usuário {0}".format(self.nome_completo())

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class TimeStampedModel(models.Model):
    """
    Essa classe contém campos de timestamps.

    Todos os models com exceção de Usuario vão
    herdar dessa classe.
    """
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Endereco(TimeStampedModel):
    """
    Model de endereço que contém um país, um estado e uma cidade.
    A principio esse momdel não contém nenhum tipo de validação.
    """

    pais = models.CharField(max_length=255, default="")
    #pais_sigla = models.CharField(max_length=3, default="")

    cidade = models.CharField(max_length=255, default="")
    #cidade_sigla = models.CharField(max_length=3, default="")

    estado = models.CharField(max_length=255, default="")
    #estado_sigla = models.CharField(max_length=3, default="")

    def __str__(self):
        return "Endereço: {0}, {1} de {2}".format(self.pais, self.cidade, self.estado)

class Tecnologia(TimeStampedModel):
    """
    Tecnologias/skills. Tecnologias são usadas para adicionar detalhes
    a cargos e vagas
    """
    nome = models.CharField(max_length=255, default = "")#nome da tecnologia
    descricao = models.TextField()#descrição da tecnologia

    def __str__(self):
        return "Tecnologia: {0}".format(self.nome)

class Cargo(TimeStampedModel):
    """
    Cargo/profissão. Cargos são usados para adicionar mais detalhes à vagas
    """
    nome = models.CharField(max_length=255, default = "")#nome do cargo
    descricao = models.TextField()#descrição do cargo
    tecnologias = models.ManyToManyField(Tecnologia,  blank = True)#tecnologias usadas nesse cargo

    def __str__(self):
        return "Cargo: {0}".format(self.nome)

class Vaga(TimeStampedModel):
    """
    Model de vagas. Todas as vagas do sistema são instância desse model

    """
    titulo = models.CharField(max_length=255, default="")#titulo para a vaga
    descricao = models.TextField(default="")#campo de descrição da vaga
    data_inicio = models.DateTimeField(auto_now_add=True)#data de inicio da vaga no sistema
    data_fim = models.DateTimeField(null=True, blank = True)#data de fim da vaga no sistema
    remuneracao = models.FloatField(default=0)#remuneracao oferecida pela vaga
    
    disponivel = models.BooleanField(default = True)#vaga ainda está disponível no sistema

    endereco = models.ForeignKey(Endereco,on_delete=models.SET_NULL,null=True, blank=True)#endereço que a vaga se refere
    cargo = models.ForeignKey(Cargo,on_delete=models.SET_NULL, null=True, blank=True)#cargo que a vaga se refere
    
    tecnologias = models.ManyToManyField(Tecnologia, blank = True)#tecnologias associadas a vaga

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)#empres que criou a vaga

    link = models.TextField(default="")# link para saber mais detalhes sobre a vaga

    def __str__(self):
        return "Vaga: {0}".format(self.titulo)