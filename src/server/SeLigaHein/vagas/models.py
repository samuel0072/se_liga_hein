from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Usuario(AbstractUser):
    """
    Modelo do usuário padrão do sistema
    """
    CANDIDATO = 'CAN'
    EMPRESA = 'EMP'
    TIPOS_USUARIOS = [
        (CANDIDATO, 'Candidato'),
        (EMPRESA, 'Empresa')
    ]

    tipo = models.CharField(max_length=3, choices=TIPOS_USUARIOS, default=CANDIDATO)#tipo do usuário, 0 para candidato e 1 para empresa
    email_2 = models.CharField(max_length=255)#o django já possui um campo de email
    telefone_1 = models.CharField(max_length=255)
    telefone_2 = models.CharField(max_length=255)
    descricao = models.TextField()#campo de bio ou descrição de uma empresa
    cnpj = models.CharField(max_length=14, default = '')#campo opcional para usuários do tipo empresa

    def nome_completo(self):
        """
        Retorna o nome completo do usuário
        """
        return "{0} {1}".format(self.first_name, self.last_name)

class TimeStampedModel(models.Model):
    """
    Essa classe contém campos de timestamps
    Todos os models com exceção de Usuario vão
    herdar dessa classe.
    """
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Vagas(TimeStampedModel):
    descricao = models.TextField()#campo de descrição da vaga
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    
