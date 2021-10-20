from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.db.models import Q

from rest_framework_simplejwt.authentication import JWTAuthentication

from vagas.serializers import *
from vagas.models import *

content_type = "aplication/json"

@api_view(['GET'])
def buscar_tecnologia(request):
    tecnologias = Tecnologia.objects.all()
    if 'id' in request.query_params:
        id = int(request.query_params['id'])
        tecnologias = Tecnologia.objects.filter(pk = id)
    elif 'nome' in request.query_params:
        nome = request.query_params['nome']
        nome = nome.split()#separa cada palavra informada por espaço, tabulações, quebras de linha...
        regex = r"(" + "|".join(nome) + ")+"#cria um regex para cada palavra do parametro
        tecnologias = Tecnologia.objects.filter(Q(nome__iregex = regex)|
                                Q(descricao__iregex = regex)|
                                Q(tag__iregex = regex))
        
    serializer = TecnologiaSerializer(tecnologias, many = True)
    return Response(serializer.data, content_type=content_type, status = status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, JWTAuthentication])
def criar_tecnologia(request):
    serializer = TecnologiaSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, content_type=content_type, status = status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication, JWTAuthentication, IsAdminUser])
def mudar_tecnologia(request):
    if request.method == 'PUT':
        id = int(request.data['id'])
        tecnologia = get_object_or_404(Tecnologia, pk=id)
        serializer = TecnologiaSerializer(tecnologia, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK, content_type=content_type)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST, content_type=content_type)
    elif request.method == 'DELETE':

        id = int(request.data["id"])

        tec = get_object_or_404(Tecnologia, pk = id)

        tec.delete()

        return Response(status=status.HTTP_200_OK)