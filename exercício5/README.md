Exercício 05 – Django: Models Pessoa, Endereço e Página de Perfil

📚 Conteúdo baseado nas aulas 8, 9 e 10 de Django.

📌 Descrição

Neste exercício eu desenvolvi os modelos Pessoa e Endereco, fiz o registro no Django Admin e montei uma página de perfil única para exibir as informações de qualquer tipo de usuário do sistema.

A estrutura ficou assim:

Pessoa ligada ao usuário do Django (ForeignKey)

Pessoa ligada ao endereço usando (OneToOneField)

Endereço com dados completos (rua, número, bairro, cidade, estado e CEP)

Todos os usuários (admin, gerente ou usuário comum) acessam a mesma página de perfil

🚀 Como rodar o projeto

Criar e ativar o ambiente virtual

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac


Instalar o Django

pip install django


Fazer as migrações

python manage.py makemigrations
python manage.py migrate


Criar um superusuário

python manage.py createsuperuser


Iniciar o servidor

python manage.py runserver


Acessar o sistema

Login: http://127.0.0.1:8000/login/

Perfil: http://127.0.0.1:8000/perfil/