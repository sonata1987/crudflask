1. Objetivo do Projeto

Este projeto consiste em uma API RESTful simples desenvolvida em Python com o framework Flask. 
Seu objetivo é construir um (CRUD) de um catálogo de livros, utilizando o SQLite como banco de dados.
Visa atender aos requisitos do projeto de Mentoria

2. Estrutura do Projeto
O projeto é dividido em dois arquivos:
data.py
Módulo responsável pela interação com o banco de dados e que contém as funções para conectar, criar a tabela livros e executar as operações.
app.py
Módulo do servidor Flask. Define as rotas HTTP e a lógica de resposta das requisições.

3. Pré-requisitos
Para rodar o projeto, você precisa ter instalado:
Python 3
Flask

4. Como Executar
Salve os códigos dos arquivos data.py e app.py na mesma pasta.
Abra o terminal na pasta do projeto.
Execute o arquivo principal: python app.py
O servidor será iniciado.
teste com postman ou insomnia

5. Endpoints da API:
Listar Todos os Livros
Método: GET
Rota: /livros
Função: data.get_livros()
Descrição: Retorna uma lista com todos os livros.

Adicionar Novo Livro
Método: POST
Rota: /livros
Função: data.add_livro()
Descrição: Adiciona um novo livro.

Atualizar Livro 
Método: PATCH
Rota: /livros/<id>
Função: data.update_livro()
Descrição: Atualiza os dados de um livro pelo seu ID.

Deletar Livro
Método: DELETE
Rota: /livros/<id>
Função: data.delete_livro()
Descrição: Remove um livro pelo seu ID.