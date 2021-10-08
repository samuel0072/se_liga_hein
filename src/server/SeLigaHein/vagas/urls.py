from django.urls import path, include
from rest_framework.authtoken import views as rest_auth_views
from vagas import views

urlpatterns = [
    path('', views.vaga, name = 'index'),
    path('listar', views.listar, name = 'listar'),
    path('cargo', views.cargo, name = 'cargo'),
    path('api-token', rest_auth_views.obtain_auth_token),#rota pra obter um token de autenticação
]
