# OliveiraTrade
Serviço de Sign in e Sign up de usuários

## Objetivo
Criar uma solução para o cliente fictício Oliveira Trade que consiste em atender o seguinte requisito: 
Uma forma de Sign in e Sign up de usuários, permitindo que seja criado um usuário no sistema, com os campos mínimos de cadastro normal para Pessoa Física, o usuário deve ser notificado que o cadastro foi concluído com sucesso e, a partir deste ponto, ser possível executar login. 

### Teste da aplicação 
https://oliveiratrade.onrender.com

### Principais tecnologias utilizadas
Python <br>
Django Framework <br>
HTML5 <br>
Bootstrap


### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Python](https://www.python.org/). <br>
Além disto é bom ter um editor/IDE para trabalhar com o código como [Pycharm](https://www.jetbrains.com/pt-br/pycharm/download/)

### 🎲 Rodando o Back End (local)

```bash
# Clone este repositório
$ git clone <https://github.com/wiverson-nogueira/OliveiraTrade>

# Acesse a pasta do projeto no terminal/cmd
$ cd OliveiraTrade

# Instale o Django Framework
$ pip install Django==4.1.3

# Instale as dependências (consulte o arquivo requirements.txt)
$ pip install django-bootstrap-v5
$ pip install django-crispy-forms

# Altere o arquivo settings.py
Comentar as linhas:
-> import dj_database_url
-> DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Realizar as migrações para o DB
$ python manage.py makemigrations
$ python manage.py migrate

# Crie um usuario para gerenciamento/acesso
$ python manage.py createsuperuser

# Execute a aplicação
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse <http://http://127.0.0.1:8000/>
```

### Autor
Feito por [Wiverson Lima](mailto:wiverson.nogueira@gmail.com) <br>
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/wiverson-lima/)](https://www.linkedin.com/in/wiverson-lima/)

