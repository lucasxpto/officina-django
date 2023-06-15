## Versão Online
[Acessar demostração on-line](https://lucaspedreira.pythonanywhere.com/)

usuário: admin

senha: 123456
***
usuário: gerente

senha: G12345678

***

# Programação III - Projeto Django

Este projeto é uma parte integral da disciplina de Programação III, oferecida no Instituto Federal de Rondônia, campus Ariquemes. A finalidade é criar uma aplicação web para gerenciar um negócio, com base em um modelo conceitual específico.

## Tecnologias Utilizadas

A aplicação foi desenvolvida utilizando:

- Python: A linguagem de programação utilizada para a lógica de back-end da aplicação.
- Django: Um framework de desenvolvimento web de alto nível, escrito em Python, que promove o rápido desenvolvimento e design limpo e pragmático.
- TailwindCSS: Uma framework de CSS de baixo nível que permite aos desenvolvedores construir designs personalizados sem restrições.
- MySQL: O sistema de gerenciamento de banco de dados utilizado para armazenar e gerenciar os dados da aplicação.

## Descrição do Projeto

O projeto envolve a criação de todas as classes Model necessárias, com seus respectivos relacionamentos, com base no modelo conceitual fornecido. As classes foram registradas na administração do site, e foram estabelecidas permissões de modo que apenas usuários do grupo 'gerentes' possam fazer qualquer registro ou alteração nas tabelas 'mecanico' e 'equipe'.

Um CRUD (Create, Read, Update, Delete) para a tela de veículo foi desenvolvido como parte deste projeto. Isso permite a gestão eficiente de veículos na aplicação.

Nota: O projeto apresenta heranças entre as classes "pessoa", "cliente" e "mecanico", bem como entre "item", "serviço" e "peça". As chaves primárias podem ser IDs gerados pelo Django ORM.

***

## Alunos
- Lucas Pedreira Vital
- Harleson da Cruz Candido
- Makalister Andrade da Silva
- Alexandre Girardello

***

## Instruções para Execução

Para executar a aplicação localmente, siga as instruções abaixo:

1. **Clone o repositório** para sua máquina local.

2. **Crie um ambiente virtual** com os seguintes comandos:
    - `python -m venv venv`
    - `source venv/bin/activate`
    - `python -m pip install --upgrade pip`

3. **Instale as dependências** usando os seguintes comandos:
    - `pip install -r requirements.txt`
    - `npm install`
    - `npx tailwindcss -i ./static/main.css -o ./static/main.min.css --watch`

4. **Execute as migrações** com o comando `python manage.py migrate`.

5. **Crie um super usuário** com o comando `python manage.py createsuperuser` e siga as instruções na tela.

6. **Execute o servidor** com o comando `python manage.py runserver`.

7. **Acesse o sistema** em `http://localhost:8000/` em seu navegador para acessar a aplicação.

Siga as instruções acima para rodar o projeto localmente. Se encontrar algum problema, não hesite em abrir uma issue no GitHub ou entrar em contato direto.
