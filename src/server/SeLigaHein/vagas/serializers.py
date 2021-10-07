from rest_framework import serializers
from .models import *

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = ['titulo', 'descricao', 'data_inicio',
        'data_fim', 'remuneracao', 'endereco',
        'cargo', 'tecnologias', 'empresa', '_id']

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['email', 'email_2', 'telefone_1', 'telefone_2',
        'descricao', 'cnpj', '_id']

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['nome', 'descricao', 'tecnologias', '_id']

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia
        fields = ['_id', 'nome', 'descricao']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['_id', 'pais', 'cidade', 'estado']

class EntidadeEnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntidadeEndereco
        fields = ['_id', 'nome', 'sigla', 'tipo']

