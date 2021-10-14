from .models import *
from datetime import datetime
from django.db.models import Q

def buscar_vaga(campos):
    vagas = Vaga.objects.none()
    if 'id' in campos:
        try:
            id = int(campos['id'])
            vagas = Vaga.objects.filter(id=id)
        except:
            pass
    else:
        filtros = {}

        if 'usuario_id' in campos:
            try:
                usuario_id = int(campos['usuario_id'])
                filtros['usuario'] = usuario_id
            except:
                pass
        if 'cargo_id' in campos:
            try:
                cargo_id = int(campos['cargo_id'])
                filtros['cargo'] = cargo_id
            except:
                pass
        if 'tecnologia_id' in campos:
            try:
                tec_id = int(campos['tecnologia_id'])
                filtros['tecnologias'] = tec_id
            except:
                pass
        if 'data_inicio' in campos:
            try:
                data_inicio = datetime.fromisoformat(campos['data_inicio'])
                filtros['data_inicio__gte'] = data_inicio
            except:
                pass
        if 'data_fim' in campos:
            try:
                data_fim = datetime.fromisoformat(campos['data_fim'])
                filtros['data_fim__lte'] = data_fim
            except:
                pass
        if 'remuneracao' in campos:
            try:
                re = float(campos['remuneracao'])
                filtros['remuneracao__gte'] = re
            except:
                pass
        if 'titulo' in campos:
            try:
                nome = campos['titulo']
                nome = nome.split()#separa cada palavra informada por espaço, tabulações, quebras de linha...
                regex = r"(" + "|".join(nome) + ")+"
                filtros['titulo__iregex'] = regex
            except:
                pass
        if 'cargo_nome' in campos:
            try:
                nome = campos['cargo_nome']
                nome = nome.split()#separa cada palavra informada por espaço, tabulações, quebras de linha...
                regex = r"(" + "|".join(nome) + ")+"
                filtros['cargo__nome__iregex'] = regex
            except:
                pass
        if 'tecnologia_nome' in campos:
            try:
                nome = campos['tecnologia_nome']
                nome = nome.split()#separa cada palavra informada por espaço, tabulações, quebras de linha...
                regex = r"(" + "|".join(nome) + ")+"
                filtros['tecnologias__nome__iregex'] = regex
            except:
                pass
        if 'usuario_nome' in campos:
            try:
                nome = campos['usuario_nome']
                nome = nome.split()#separa cada palavra informada por espaço, tabulações, quebras de linha...
                regex = r"(" + "|".join(nome) + ")+"
                filtros['usuario__first_name__iregex'] = regex
                filtros['usuario__last_name__iregex'] = regex
            except:
                pass
        if 'endereco' in campos:
            try:
                nome = campos['endereco']
                nome = nome.split()#separa cada palavra informada por espaço, tabulações, quebras de linha...
                regex = r"(" + "|".join(nome) + ")+"
                filtros['endereco__pais__iregex'] = regex
                filtros['endereco__cidade__iregex'] = regex
                filtros['endereco__estado__iregex'] = regex
            except:
                pass
        
        filtros['disponivel'] = True
        
        q = Q(**filtros)
        q.connector = Q.AND
        vagas = Vaga.objects.filter(q).order_by('-updated_at')
    return vagas