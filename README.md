# 📚 Sistema de Biblioteca com Python, PostgreSQL e SQLAlchemy

Este projeto implementa uma aplicação para gerenciamento de empréstimos de livros em uma biblioteca, utilizando modelagem relacional com SQLAlchemy e integração com um banco de dados PostgreSQL.

## 🔧 Tecnologias Utilizadas

- Python 3.8+
- PostgreSQL
- SQLAlchemy
- psycopg2

## 📁 Estrutura do Projeto

```
biblioteca/
├── db.py                        # Configuração da conexão com o banco
├── main.py                      # Script principal de testes
│
├── models/                      # Classes ORM (entidades do banco)
│   ├── __init__.py
│   ├── aluno.py
│   ├── livro.py
│   ├── exemplar.py
│   ├── emprestimo.py
│   └── emprestimo_exemplar.py
│
└── services/                    # Operações CRUD
    ├── __init__.py
    ├── aluno_service.py
    ├── livro_service.py
    ├── exemplar_service.py
    ├── emprestimo_service.py
    └── emprestimo_exemplar_service.py
```

## ⚙️ Pré-requisitos

- PostgreSQL instalado e rodando localmente.
- Criar um banco chamado `biblioteca_db`.
- Atualizar o arquivo `db.py` com suas credenciais:

```python
DATABASE_URL = "postgresql+psycopg2://usuario:senha@localhost:5432/biblioteca_db"
```

- Instalar as dependências:

```bash
pip install sqlalchemy psycopg2
```

## 🗃️ Criação das Tabelas

Este projeto **não cria as tabelas automaticamente**. Você deve criar previamente o esquema no PostgreSQL com base na modelagem relacional descrita na Etapa 1 do trabalho.

## ▶️ Executando o Projeto

Para testar o funcionamento:

```bash
python biblioteca/main.py
```

O script irá:
- Inserir um aluno de teste
- Listar todos os alunos cadastrados

## 🛠️ Operações CRUD

Cada entidade possui um arquivo de serviço responsável pelas operações:
- `criar_<entidade>`
- `listar_<entidade>s`
- `buscar_por_id`
- `atualizar_<entidade>`
- `remover_<entidade>`

## 📌 Observações

- O projeto segue as boas práticas de separação de responsabilidades (modelos, serviços e camada de teste).
- A tabela `itememprestimo` implementa a relação N:N entre empréstimos e exemplares.