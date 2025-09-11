# Exercícios Django com Bootstrap

Projeto contendo dois exercícios práticos desenvolvidos com Django e estilizados com Bootstrap.

## 📚 Descrição dos Exercícios

### 📘 Exercício 1 – Telas com Bootstrap

#### ✅ Objetivo
Criar diversas páginas funcionais com rotas no Django utilizando o framework Bootstrap para estilização.

#### 🧩 Funcionalidades Desenvolvidas

- Tela de Login
- Tela de Logout
- Tela de Recuperação de Senha
- Tela de Alteração de Senha
- Tela de Cadastro
- Tela de Perfil
- Tela Home
- Página de Erro 404 (Página não encontrada)
- Página de Erro 403 (Acesso não permitido)
- Página de Erro 500 (Erro interno no servidor)

As páginas foram criadas com rotas usando Django, formulários HTML estilizados com Bootstrap, e com mensagens de erro personalizadas.

---

### 📘 Exercício 2 – CRUD com Modelos Django

#### ✅ Objetivo
Modelar e cadastrar dados de uma pessoa utilizando Django e exibir os dados em uma página.

#### 🧩 Funcionalidades Desenvolvidas

- **Criação do modelo `Pessoa`** com os seguintes campos:
  - Nome
  - CPF
  - E-mail
  - Telefone
  - Data de nascimento
  - RG
  - Endereço
  - Bairro

- **Registro do modelo no Django Admin** para permitir visualização e gerenciamento dos dados.

- **Criação de uma view personalizada** para acessar os dados cadastrados.

- **Construção de um template HTML com Bootstrap** para exibir os dados de maneira visual e organizada.

- **Tela de login reaproveitada** para exibir os dados digitados no prompt de comando, a fim de testar a autenticação simples.

---

## 🚀 Tecnologias Utilizadas

- Python 3
- Django
- HTML5
- CSS3 (via Bootstrap 5)
- SQLite (banco de dados padrão do Django)

---

## 💻 Como Rodar o Projeto

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

# Acesse o diretório
cd nome-do-projeto

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
source venv/bin/activate  # macOS / Linux
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações
python manage.py migrate

# Rode o servidor
python manage.py runserver
