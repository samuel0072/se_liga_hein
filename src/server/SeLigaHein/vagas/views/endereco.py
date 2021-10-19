from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

from rest_framework_simplejwt.authentication import JWTAuthentication

from vagas.serializers import *
from vagas.models import *

content_type = "aplication/json"

@api_view(['GET'])
def buscar_end(request):
    enderecos = Endereco.objects.all()
    if 'id' in request.query_params:
        id = int(request.query_params['id'])
        enderecos = Endereco.objects.filter(pk = id)
    elif 'nome' in request.query_params:
        nome = request.query_params['nome']
        nome = nome.split()#separa cada palavra informada por espaço, tabulações, quebras de linha...
        regex = r"(" + "|".join(nome) + ")+"#cria um regex para cada palavra do parametro
        enderecos = Endereco.objects.filter(Q(pais__iregex = regex)|
                                Q(cidade__iregex = regex)|
                                Q(estado__iregex = regex))
        
    serializer = EnderecoSerializer(enderecos, many = True)
    return Response(serializer.data, content_type=content_type, status = status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, JWTAuthentication])
def criar_endereco(request):
    serializer = EnderecoSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, content_type=content_type, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, JWTAuthentication])
def excluir_end(request):
    id = int(request.data["id"])

    end = get_object_or_404(Endereco, pk = id)

    end.delete()

    return Response(status=status.HTTP_200_OK)