from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import *
from .models import *

# Create your views here.
content_type = "aplication/json"

@api_view(['GET'])
def listar(request):
    #TODO: Adicionar filtros listado em docs/README.md
    vagas = Vaga.objects.all()
    serializer = VagaSerializer(vagas, many = True)
    return Response(serializer.data, content_type=content_type)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, JWTAuthentication])
def vaga(request):
    
    serializer = VagaSerializer(data = request.data)
    if serializer.is_valid():
        vaga = serializer.save()
        #adiciona o usuario a vaga que está sendo criada
        vaga.usuario = request.user
        vaga.save()
        serializer = VagaSerializer(vaga)
        return Response(serializer.data, content_type=content_type, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, JWTAuthentication])
def mudar_vaga(request):
    
    if request.method == 'PUT':
        id = int(request.data["id"])
        vaga = get_object_or_404(Vaga, pk = id)
        serializer = VagaSerializer(vaga, data = request.data)
        if serializer.is_valid():
            if (vaga.usuario != None) and ((vaga.usuario == request.user) or (request.user.is_superuser)):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        id = int(request.data["id"])
        vaga = get_object_or_404(Vaga, pk = id)

        if (vaga.usuario != None) and ((vaga.usuario == request.user) or (request.user.is_superuser)):
            vaga.delete(keep_parents=True)
            return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)


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
@authentication_classes([TokenAuthentication, JWTAuthentication])
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