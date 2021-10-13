from django.urls import path, include
from rest_framework.authtoken import views as rest_auth_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from vagas import views

app_name = 'vagas'

urlpatterns = [
    path('', views.vaga, name = 'vaga'),
    path('listar', views.listar, name = 'listar'),
    path('mudar_vaga', views.mudar_vaga, name='mudar_vaga'),
    path('cargo', views.cargo, name = 'cargo'),
    path('cargo/buscar', views.cargo_buscar, name = 'cargo_buscar'),

    path('api/auth_token', rest_auth_views.obtain_auth_token, name="auth_token"),#rota pra obter um token de autenticação
    path('api/jwt_token', TokenObtainPairView.as_view(), name='jwt_token_obtain_pair'),#rota para obter um jwt para autenticação
    path('api/jwt_token/refresh', TokenRefreshView.as_view(), name='jwt_token_refresh'),#rota para atualizar um jwt expirado para autenticação
]
