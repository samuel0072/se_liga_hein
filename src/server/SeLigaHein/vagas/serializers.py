from rest_framework import serializers
from .models import *

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = ['titulo', 'descricao', 'data_inicio',
        'data_fim', 'remuneracao', 'endereco',
        'cargo', 'tecnologias', 'usuario', 'link', 'id']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email', 'email_2', 'telefone_1', 'telefone_2',
        'descricao', 'id', 'first_name', 'last_name']#first_name e last_name já são campos do model AbstractUser do django

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        #depth = 2
        fields = ['nome', 'descricao', 'tecnologias', 'id']

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = ['id', 'nome', 'descricao']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'pais', 'cidade', 'estado', 'pais_sigla', 'cidade_sigla', 'estado_sigla']


