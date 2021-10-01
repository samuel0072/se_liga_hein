# Rotas
## Vagas :briefcase:
> Rotas usadas para manipular objetos do tipo Vaga

`vagas/listar/todas` : lista todas as vagas do sistema

`vagas/listar/{empresa_id}/empresa`: lista todas as vagas de uma empresa especificada por empresa_id

`vagas/listar/{cargo_id}/cargo`: lista todas as vagas associadas a um determinado cargo

`vagas/listar/{tec_id}/tecnologia`: lista todas as vagas associadas a uma determinada tecnologia

`vagas/listar/{data_inicio}/data_inicio `: lista todas as vagas a partir de uma determinada data de inicio

`vagas/listar/{data_fim}/data_fim `: lista todas as vagas até uma determinada data de fim

`vagas/listar/{data_inicio}/data_inicio/{data_fim}/data_fim `: lista todas as vagas com dats entre data inicio e data fim

`vagas/listar/{endereco_id}/endereco`: Lista todas as vagas com endereço igual ao informado

`vagas/listar/{remuneracao}/remuneracao `: lista todas as vagas com uma remuneração maior igual que a informada

`vagas/buscar/{titulo}/titulo`: busca todas as vagas com o titulo parecido ao informado

`vagas/buscar/{cargo_nome}/cargo`: busca todas as vagas com o nome do cargo parecido ao informado

`vagas/buscar/{tecnologia_nome}/tecnologia`: busca todas as vagas com nome das tecnologias parecidas à informada

`vagas/bucar/{empresa_nome}/empresa`: busca todas as vagas com o nome da empresa parecido ao informado

> Todas as rotas acima só aceitam requisições GET

`vagas/criar`: 
POST: cria uma vaga e retorna seu id

`vagas/{id}`: 
GET: obtem a vaga especificada no id
PUT: atualiza a vaga especificada pelo id
DELETE: deleta a vaga especificada pelo id

`vagas/{id}/tec/{tec_id}` :
PUT: adiciona uma tecnologia a uma vaga
DELETE: remove a tecnologia da vaga

`vagas/{id}/cargo/{cargo_id}` :
PUT: muda a vaga com o cargo especificado

`vagas/{id}/cidade/{cidade_id}` :
PUT: muda a cidade do endereço da vaga

`vagas/{id}/estado/{estado_id}` :
PUT: muda o estado do endereço da vaga

`vagas/{id}/pais/{pais_id}`:
PUT: muda o país do endereço da vaga

`vagas/{id}/remuneracao/{remuneracao}` :
PUT: muda a remuneracao da vaga 

`vagas/{id}/data_inicio/{data_inicio}` :
PUT: muda a data de inicio da vaga

`vagas/{id}/data_fim/{data_fim}` :
PUT: muda a data de inicio da vaga



# Organização do banco de dados
![Imagem do banco de dados. O banco foi modelagem usando uma abordagem relacional](modelagem_db.png)