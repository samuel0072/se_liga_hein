from django.urls import path, include
from vagas import views

urlpatterns = [
    path('', views.vaga, name = 'index'),
    path('api-auth/', include('rest_framework.urls')),
    path('listar/', views.listar, name = 'listar'),
]
