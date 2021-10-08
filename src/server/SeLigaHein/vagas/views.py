from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from rest_framework import response

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer

from .serializers import *
from .models import *

# Create your views here.
content_type = "aplication/json"

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
#@authentication_classes([TokenAuthentication])
def listar(request):
    #TODO: Adicionar filtros listado em docs/README.md
    vagas = Vaga.objects.all()
    serializer = VagaSerializer(vagas, many = True)
    return Response(serializer.data, content_type=content_type)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def vaga(request):
    
    if request.method == 'GET':
        
        id = request.query_params["id"]
        vaga = get_object_or_404(Vaga, pk=id)#TODO: está retornando text/html quando não encontra, mudar para aplication/json
       
        serializer = VagaSerializer(vaga)
        return Response(serializer.data, content_type=content_type)
        
            
    if request.method == 'POST':
        serializer = VagaSerializer(data = request.data)

        if serializer.is_valid() and request.user.tipo == Usuario.EMPRESA:
            serializer.save()
            return Response(serializer.data, content_type=content_type, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass

@api_view(['GET'])
def cargo_buscar(request):

    if "cargo_id" in request.query_params:#se já for informado o id do cargo, a busca por tec_id e nome é dispensada
        cargo_id = int(request.query_params["cargo_id"])
        cargo = get_object_or_404(Cargo, pk = cargo_id)
        serializer = CargoSerializer(cargo)
    
    else:
        cargos = Cargo.objects.all()#por padrão retorna todos os cargos, com paginação

        if "tec_id" in request.query_params:
            tec_id = int(request.query_params["tec_id"])
            tec = get_object_or_404(Tecnologia, pk = tec_id)
            cargos = cargos.filter(tecnologias = tec)
        
        if "nome" in request.query_params:
            nome = str(request.query_params["nome"])

            nome = nome.split()#separa cada palavra informada por espaço, tabulações, quebras de linha...

            regex = r"(" + "|".join(nome) + ")+"#cria um regex do tipo: (palavra1|palavra2|palavra3|...)

            cargos = cargos.filter(nome__iregex=regex)
        
        serializer = CargoSerializer(cargos, many = True)

    return Response(serializer.data, status = status.HTTP_200_OK, content_type=content_type)


@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def cargo(request):

    if not request.user.is_superuser:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'POST':
        serializer = CargoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, content_type=content_type, status = status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        id = int(request.data["id"])
        cargo = get_object_or_404(Cargo, pk = id)
        serializer = CargoSerializer(cargo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        id = int(request.data["id"])
        cargo = get_object_or_404(Cargo, pk = id)
        cargo.delete(keep_parents=True)
        return Response(status=status.HTTP_200_OK)