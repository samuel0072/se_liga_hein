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
    email_2 = models.CharField(max_length=255, null=True, blank=True)#o django já possui um campo de email
    telefone_1 = models.CharField(max_length=255)
    telefone_2 = models.CharField(max_length=255, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)#campo de bio ou descrição de uma empresa
    cnpj = models.CharField(max_length=14, default = '', null=True, blank=True)#campo opcional para usuários do tipo empresa

    def nome_completo(self):
        """
        Retorna o nome completo do usuário
        """
        return "{0} {1}".format(self.first_name, self.last_name)

    def __str__(self):
        return "Usuário {0}: {1}".format(self.nome_completo(), self.get_tipo_display())

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


class EntidadeEndereco(TimeStampedModel):
    """
    Model de entidade de um endereço.

    Esse model pode representar um país, estado ou cidade.
    """
    PAIS = 'PS'
    ESTADO = 'ET'
    CIDADE = 'CD'
    TIPOS_CIDADE = [
        (PAIS, 'País'),
        (ESTADO, 'Estado'),
        (CIDADE, 'Cidade')
    ]
    nome = models.CharField(max_length=255)
    sigla = models.CharField(max_length=3)
    tipo = models.CharField(choices=TIPOS_CIDADE, default=PAIS, max_length=2)

    def __str__(self):
        return "Entidade Endereço: {0}-{1} do tipo {2}".format(self.nome, self.sigla, self.get_tipo_display())

class Endereco(TimeStampedModel):
    """
    Model de endereço que contém um país, um estado e uma cidade.
    """
    pais = models.ForeignKey(EntidadeEndereco, on_delete=models.PROTECT, related_name='pais')
    cidade = models.ForeignKey(EntidadeEndereco, on_delete=models.PROTECT, related_name='cidade')
    estado = models.ForeignKey(EntidadeEndereco, on_delete=models.PROTECT, related_name='estado')

    def __str__(self):
        return "Endereço: {0}, {1} de {2}".format(self.pais.nome, self.cidade.nome, self.estado.nome)

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
    tecnologias = models.ManyToManyField(Tecnologia)#tecnologias usadas nesse cargo

    def __str__(self):
        return "Cargo: {0}".format(self.nome)

class Vaga(TimeStampedModel):
    """
    Model de vagas. Todas as vagas do sistema são instância desse model

    """
    titulo = models.CharField(max_length=255, default="")#titulo para a vaga
    descricao = models.TextField()#campo de descrição da vaga
    data_inicio = models.DateTimeField(auto_now_add=True)#data de inicio da vaga no sistema
    data_fim = models.DateTimeField()#data de fim da vaga no sistema
    remuneracao = models.FloatField(default=0)#remuneracao oferecida pela vaga
    
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT, null=True, blank=True)#endereço que a vaga se refere
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, null=True, blank=True)#cargo que a vaga se refere
    
    tecnologias = models.ManyToManyField(Tecnologia)#tecnologias associadas a vaga

    empresa = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True, blank=True)#empres que criou a vaga

    def __str__(self):
        return "Vaga: {0}. Empresa associada: {1}".format(self.titulo, self.empresa.first_name)