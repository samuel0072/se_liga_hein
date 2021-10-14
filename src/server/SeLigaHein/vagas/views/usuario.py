from django.shortcuts import get_object_or_404
from django.core import exceptions
from django.db import transaction
import django.contrib.auth.password_validation as validators
from django.db import IntegrityError, DatabaseError
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from vagas.serializers import *
from vagas.models import *
from vagas.translations import pt_br#TODO:mudar pra carregar as traduções com a inicialização do sistema e que seja possível o 'usuário' escolher


# Create your views here.
content_type = "aplication/json"


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, JWTAuthentication])
def usuario(request):
    if request.method == "GET":
        serializer = UsuarioSerializer(request.user)
        return Response(serializer.data, status = status.HTTP_200_OK, content_type=content_type)
    
    elif request.method == 'PUT':
        serializer = UsuarioSerializer(request.user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK, content_type=content_type)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def registrar(request):
    erro_dict = {}#dicionario para caso haja erro
    serializer = None
    erro_status = status.HTTP_400_BAD_REQUEST
    
    try:
        serializer = UsuarioSerializer(data = request.data)
        if not serializer.is_valid():
            erro_dict['erros'] = serializer.errors
            raise Exception()
        
        confirmar_senha = request.data["confirmar_senha"]
        senha = request.data["senha"]

        # confere a senha
        if senha != confirmar_senha:
            raise exceptions.ValidationError(pt_br.ERRO_SENHA_CONFIRMAR_SENHA)

        with transaction.atomic():
            # cria o usuário com os campos obrigatórios
            usuario = Usuario(username=request.data["username"],
                        first_name=request.data["first_name"],
                        last_name=request.data["last_name"],
                        email=request.data["email"])
            
            #adiciona os campos opicionais
            if 'telefone_1' in request.data:
                usuario.telefone_1 = request.data['telefone_1']
            if 'telefone_2' in request.data:
                usuario.telefone_2 = request.data['telefone_2']
            if 'email_2' in request.data:
                usuario.email_2 = request.data['email_2']
            if 'descricao' in request.data:
                usuario.descricao = request.data['descricao']

            serializer = UsuarioSerializer(usuario)#atualiza com o id do usuario
            validators.validate_password(senha, user=Usuario)  # valida a senha
            usuario.set_password(senha)  # define senha
            usuario.clean_fields()  # valida os demais campos
            usuario.save()  # salva o usuário na base
            return Response(serializer.data, status=status.HTTP_200_OK, content_type=content_type) 
    except exceptions.ValidationError as e:
        # Erros dos outros campos
        if hasattr(e, 'message_dict'):
            for key, value in e.message_dict.items():
                erro_dict[key] = value[0]
        # Erros da senha
        else:
            erro_dict['senha'] = list(e.messages)
        #temp.delete()
    # caso já exista um usuario com mesmo username
    except IntegrityError:
        erro_dict['username'] = pt_br.ERRO_USERNAME_EXISTE
    except MultiValueDictKeyError:
       erro_dict['campos'] =  pt_br.ERRO_CAMPOS_VAZIOS
    except DatabaseError:
        erro_dict['database'] =  pt_br.ERRO_CRIAR_USUARIO_DATABASE
        erro_status = status.HTTP_500_INTERNAL_SERVER_ERROR
    except:
        erro_dict['mensagem'] =  pt_br.ERRO_INESPERADO
    
    erro_dict['dados'] = serializer.data
    return Response(erro_dict, status=erro_status, content_type=content_type)

