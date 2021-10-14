from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from vagas.serializers import *
from vagas.models import *
from vagas.utils import buscar_vaga


# Create your views here.
content_type = "aplication/json"

@api_view(['GET'])
def listar(request):
    vagas = buscar_vaga(request.query_params)
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
    id = int(request.data["id"])
    vaga = get_object_or_404(Vaga, pk = id)
    
    if (vaga.usuario != None) and ((vaga.usuario == request.user) or (request.user.is_superuser)):
        if request.method == 'PUT':
            serializer = VagaSerializer(vaga, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'DELETE':
            vaga.delete(keep_parents=True)
            return Response(status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(status=status.HTTP_401_UNAUTHORIZED)