# 📋 TodoAppDjango

Sistema web para **gerenciamento de tarefas**, desenvolvido com **Python e Django**, com interface responsiva utilizando **Tailwind CSS**.

A aplicação implementa operações completas de gerenciamento de tarefas, integração com o **Django ORM**, persistência em banco de dados e painel administrativo, seguindo a arquitetura **MVT (Model-View-Template)** do Django.

---

## ✨ Funcionalidades

* 📋 **Listagem de tarefas** — visualização organizada das tarefas cadastradas.
* ➕ **Criação de tarefas** — cadastro de novos itens.
* ✏️ **Edição de tarefas** — atualização dos dados de uma tarefa existente.
* 🗑️ **Exclusão de tarefas** — remoção de registros.
* 🎨 **Interface responsiva** — adaptação para diferentes tamanhos de tela utilizando Tailwind CSS.
* 🛠️ **Painel administrativo** — gerenciamento dos registros através do Django Admin.
* 🗄️ **Persistência de dados** — armazenamento utilizando o ORM do Django.
* 🔄 **Migrações** — controle da evolução da estrutura do banco de dados.

---

## 🏗️ Arquitetura

O projeto utiliza a arquitetura **MVT (Model-View-Template)**:

```text
┌─────────────────────┐
│       Usuário       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│        URLs         │
│      Roteamento     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│        Views        │
│   Lógica da aplicação│
└───────┬───────┬─────┘
        │       │
        ▼       ▼
┌───────────┐ ┌──────────────┐
│   Forms   │ │   Templates  │
│ Validação │ │   Interface  │
└─────┬─────┘ └──────────────┘
      │
      ▼
┌─────────────────────┐
│       Models        │
│     Django ORM      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      Database       │
│       SQLite        │
└─────────────────────┘
```

Essa estrutura separa as responsabilidades da aplicação e facilita sua manutenção e evolução.

---

## 🛠️ Stack Tecnológica

| Camada         | Tecnologia       |
| -------------- | ---------------- |
| Linguagem      | Python 3.12+     |
| Framework      | Django 5.2.3     |
| Backend        | Django           |
| ORM            | Django ORM       |
| Banco de dados | SQLite           |
| Frontend       | HTML5            |
| Estilização    | Tailwind CSS     |
| Templates      | Django Templates |
| Versionamento  | Git              |

---

## 📁 Estrutura do Projeto

```text
TodoAppDjango/
│
├── manage.py
├── db.sqlite3
│
├── projeto/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
└── todo/
    ├── migrations/
    │   └── ...
    │
    ├── templates/
    │   └── ...
    │
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    └── views.py
```

### Principais componentes

* **`models.py`** — define a estrutura dos dados e sua representação através do Django ORM.
* **`views.py`** — contém a lógica responsável pelo processamento das requisições.
* **`forms.py`** — responsável pela criação e validação dos formulários.
* **`urls.py`** — define o roteamento das requisições.
* **`templates/`** — contém as páginas HTML utilizadas pela aplicação.
* **`admin.py`** — configura a integração do modelo com o Django Admin.
* **`migrations/`** — mantém o histórico das alterações estruturais do banco de dados.
* **`settings.py`** — concentra as configurações principais do projeto.
* **`manage.py`** — principal ferramenta de gerenciamento do projeto Django.

---

## ⚙️ Requisitos

Antes de executar o projeto, tenha instalado:

* **Python 3.12 ou superior**
* **pip**
* **Git**

[Python — Download oficial](https://www.python.org/downloads/?utm_source=chatgpt.com)

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/TodoAppDjango.git
cd TodoAppDjango
```

### 2. Crie um ambiente virtual

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Caso o projeto não possua um `requirements.txt`:

```bash
pip install django
```

### 4. Execute as migrações

```bash
python manage.py migrate
```

### 5. Inicie o servidor

```bash
python manage.py runserver
```

A aplicação estará disponível em:

```text
http://127.0.0.1:8000/
```

---

## 🛠️ Django Admin

O projeto também utiliza o painel administrativo nativo do Django.

Para criar um usuário administrador:

```bash
python manage.py createsuperuser
```

Depois, acesse:

```text
http://127.0.0.1:8000/admin/
```

O Django Admin permite administrar os registros diretamente através da interface administrativa.

---

## 🖥️ Interface

A aplicação utiliza **Tailwind CSS** para construção da interface, proporcionando uma estrutura responsiva e consistente.

As principais operações disponíveis são:

```text
┌───────────────────────────────┐
│          Tarefas               │
├───────────────────────────────┤
│ ✓ Estudar Django      Editar  │
│ ✓ Desenvolver projeto  Excluir│
│ ✓ Revisar código       Editar  │
├───────────────────────────────┤
│       + Nova tarefa            │
└───────────────────────────────┘
```

O fluxo principal da aplicação é baseado em operações **CRUD**:

**Create → Read → Update → Delete**

---

## 🔐 Configuração para Produção

Para utilizar o projeto em um ambiente de produção, algumas configurações devem ser ajustadas.

### `SECRET_KEY`

A chave secreta deve ser armazenada de maneira segura, preferencialmente através de variáveis de ambiente.

### `DEBUG`

Em produção:

```python
DEBUG = False
```

### `ALLOWED_HOSTS`

Os domínios e endereços utilizados pela aplicação devem ser definidos explicitamente:

```python
ALLOWED_HOSTS = [
    "seu-dominio.com",
]
```

Também é recomendável utilizar um banco de dados apropriado para produção, como **PostgreSQL**.

---

## 🔮 Possíveis Evoluções

A arquitetura atual permite a expansão do sistema para funcionalidades mais completas, como:

* 🔐 Autenticação e autorização de usuários.
* 👤 Tarefas associadas individualmente a cada usuário.
* 📅 Datas de criação, vencimento e conclusão.
* 🏷️ Categorias e etiquetas.
* 🔎 Pesquisa e filtros.
* 📊 Dashboard com métricas das tarefas.
* 🌐 API REST com Django REST Framework.
* 🐘 Migração para PostgreSQL.
* 🧪 Testes automatizados.
* 🐳 Containerização com Docker.
* ☁️ Deploy em serviços de cloud.

---

## 📄 Licença

Este projeto é distribuído sob a licença **MIT**.

Consulte o arquivo [`LICENSE`](LICENSE) para obter os termos completos da licença.

---

## 👨‍💻 Autor

**Filipe Silva**

[GitHub — filipesilva-dev]([https://github.com/oTyR3D])

---

> Projeto desenvolvido como aplicação prática de desenvolvimento web com Django.
