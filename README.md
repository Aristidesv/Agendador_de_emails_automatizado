# Agendador-de-emails-automatizado

Este é um projeto simples de um **agendador de e-mails** desenvolvido com Python,Flask e SQLite.
Ele permite que usuários agendem o envio de e-mails com data e hora específicas, e o sistema cuida do envio automático utilizando o **SMTP do Gmail**.

## Funcionalidades

- Agendar envio de e-mails com data e hora específicas
- Envio automático em segundo plano
- Visualização do status do e-mail (Agendado ou Enviado)
- Interface web responsiva com **Bootstrap**
- Banco de dados local com **SQLite**

## Interface Web

A interface web permite:

- Cadastro de destinatário, assunto, corpo da mensagem e data/hora do envio
- Visualização em tabela dos e-mails agendados
- Atualização do status após o envio

Na interface utilizei **Bootstrap** para deixar o layout limpo e simples


## Requisitos
- Conta do Gmail com "senha de app" ativada



## Instalação

### 1. Clonar o projeto
### 2. Criar e ativar o ambiente virtual:
## No terminal do projecto execute os comandos
python3 -m venv venv

source venv/bin/activate    # Linux 

venv\Scripts\activate     # Windows
### 3. Instale as dependencias
pip install riquisitos.txt
### 4. Configurar envio com Gmail
 Precisa gerar uma senha de aplicativo no Gmail:
 Acesse: https://myaccount.google.com/security
 Ative a verificação em duas etapas
 Vá até “Senhas de app” e gere uma senha
 Use essa senha no lugar da sua senha normal no código

### Executando a aplicação
1. Iniciar a interface
   python app.py

Acesse no navegador:
http://localhost:5000
2. Abrir outro terminal, iniciar o agendador
python scheduler.py

Depois disso e so usar o ser sistema a vontade........













