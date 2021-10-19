from django.urls import path, include
from rest_framework.authtoken import views as rest_auth_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from vagas.views import *

app_name = 'vagas'

urlpatterns = [
    path('', vaga.vaga, name = 'vaga'),
    path('listar', vaga.listar, name = 'listar'),
    path('mudar_vaga', vaga.mudar_vaga, name='mudar_vaga'),
    path('cargo', cargo.cargo, name = 'cargo'),
    path('cargo/buscar', cargo.cargo_buscar, name = 'cargo_buscar'),
    path('cargo/criar', cargo.criar_cargo, name = 'cargo_criar'),
    path('usuario', usuario.usuario, name = 'usuario'),
    path('usuario/registrar', usuario.registrar, name = 'registrar'),
    path('endereco', endereco.criar_endereco, name = 'criar_endereco'),
    path('endereco/buscar', endereco.buscar_end, name = 'buscar_endereco'),
    path('endereco/excluir', endereco.excluir_end, name = 'excluir_endereco'),

    path('api/auth_token', rest_auth_views.obtain_auth_token, name="auth_token"),#rota pra obter um token de autenticação
    path('api/jwt_token', TokenObtainPairView.as_view(), name='jwt_token_obtain_pair'),#rota para obter um jwt para autenticação
    path('api/jwt_token/refresh', TokenRefreshView.as_view(), name='jwt_token_refresh'),#rota para atualizar um jwt expirado para autenticação

]
