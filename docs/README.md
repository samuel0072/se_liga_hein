# Rotas
## Vagas :briefcase:
> Rotas usadas para manipular objetos do tipo Vaga

`vagas/listar` : lista vagas filtradas de acordo com os parametros da requisição

GET - Paramêtros da requisição:

    - empresa: lista todas as vagas de uma empresa especificada por empresa_id
    - cargo: lista todas as vagas associadas a um determinado cargo
    - tecnologia: lista todas as vagas associadas a uma determinada tecnologia
    - data_inicio: lista todas as vagas a partir de uma determinada data de inicio
    - data_fim: lista todas as vagas até uma determinada data de fim
    - endereco: Lista todas as vagas com endereço igual ao informado
    - remuneracao: lista todas as vagas com uma remuneração maior igual que a informada
    - sem paramêtros: lista todas as vagas do sistema
    - titulo: busca todas as vagas com o titulo parecido ao informado
    - cargo_nome: busca todas as vagas com o nome do cargo parecido ao informado
    - tecnologia_nome: busca todas as vagas com nome das tecnologias parecidas à informada
    - empresa_nome: busca todas as vagas com o nome da empresa parecido ao informado

> Todas as rotas acima só aceitam requisições GET

`vagas/`: 

GET - Paramêtros da requisição:

    - id: Obtem a vaga especificada pelo id e lista todos os que se candidataram à  vaga

POST: cria uma vaga e retorna seu id

PUT - Corpo da requisição:

    - tec_id: adiciona uma tecnologia a uma vaga
    - cargo_id: muda a vaga com o cargo especificado
    - cidade_id: muda a cidade do endereço da vaga
    - estado_id: muda o estado do endereço da vaga
    - pais_id: muda o país do endereço da vaga
    - remuneracao: muda a remuneracao da vaga 
    - data_inicio: muda a data de inicio da vaga
    - data_fimmuda a data de fim da vaga

DELETE - Corpo da requisição:

    - vaga_id: Excluí a vaga especificada
    - tec_id: remove a tecnologia da vaga

`vagas/{id}/candidatar`:
POST: O usuário logado se candidata à vaga

## Usuários :busts_in_silhouette:

`vagas/usuario/{id}`:
GET: Retorna as informações públicas do usuário informado

`vagas/usuario/criar`:
POST: Cria um usuário e o retorna

`vagas/usuario/login`:
POST: loga um usuário no sistema

`vagas/usuario/logout`:
POST: desloga o usuário do sistema

`vagas/usuario/editar`:
PUT: Atualiza as informações públicas do usuário logado

`vagas/usuario/senha/editar`:
POST: Altera a senha do usuário logado

`vagas/usuario/senha/esquecer/{username}`:
POST: Envia um email para o usuário informado em username com a nova senha gerada pela sistema

## Cargos


`vagas/cargo/{id}`:
GET: Retorna o cargo especificado
DELETE: Excluí o cargo, somente para administrador do sistema

`vagas/cargo/{tec_id}/tecnologia`:
GET: Retorna cargos que possuem a tecnologia informada pelo id

`vagas/cargo/{nome}/nome`:
GET: Retorna cargos que possuem nomes semelhantes ao informado

> Rotas abaixo disponíveis somente para o adiministrador do sistema

`vagas/cargo/criar`:
POST: Cria um cargo e o retorna

`vagas/cargo/{id}/editar`:
PUT: Atualiza as informações do cargo logado


## Tecnologia

`vagas/tec/{id}`:
GET: Retorna a tecnologia especificada
DELETE: Excluí a tecnologia, somente para administrador do sistema

`vagas/tec/{nome}/nome`:
GET: Retorna tecnologias que possuem nomes semelhantes ao informado

> Rotas abaixo disponíveis somente para o adiministrador do sistema

`vagas/tec/criar`:
POST: Cria uma tecnologia e a retorna

`vagas/tec/{id}/editar`:
PUT: Atualiza as informações da tecnologia logado

## Endereço

`vagas/endereco/{id}`:
GET: Retorna o endereço especificada
DELETE: Excluí o endereço, somente para administrador do sistema

`vagas/endereco/entidade/{id}`:
GET: Retorna a entidade de endereço especificada
DELETE: Excluí a entidade de endereço especificada, , somente para administrador do sistema

`vagas/endereco/entidade/{nome}/nome`:
GET: Retorna as entidades de endereço com nomes semelhantes ao informado

`vagas/endereco/entidade/{sigla}/sigla`:
GET: Retorna as entidades de endereço com sigla igual a informada

> Rotas abaixo disponíveis somente para o adiministrador do sistema

`vagas/endereco/criar`:
POST: Cria um endereço e o retorna

`vagas/endereco/criar/entidade`:
POST: Cria uma entidade de endereço e a retorna

# Organização do banco de dados
![Imagem do banco de dados. O banco foi modelagem usando uma abordagem relacional](modelagem_db.png)