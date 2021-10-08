from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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
        vaga = Vaga.objects.get(pk=id)
        serializer = VagaSerializer(vaga)
        
        return Response(serializer.data, content_type=content_type)
            
    if request.method == 'POST':
        serializer = VagaSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, content_type=content_type, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass