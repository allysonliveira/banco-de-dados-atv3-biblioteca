# Sistema de Biblioteca com Python, PostgreSQL e SQLAlchemy

Este projeto implementa uma aplicação de gerenciamento de uma biblioteca utilizando SQLAlchemy (ORM) com PostgreSQL. O sistema segue todas as instruções propostas na Etapa 2 do trabalho da disciplina de Banco de Dados (UFRN).

## O que foi solicitado na Etapa 2 do Trabalho

### 1. Utilizar SQLAlchemy para mapear tabelas em classes Python (ORM)
- Local: Pasta `models/`
- Foram criadas as classes:
  - `Aluno` → `models/aluno.py`
  - `Livro` → `models/livro.py`
  - `Exemplar` → `models/exemplar.py`
  - `Emprestimo` → `models/emprestimo.py`
  - `EmprestimoExemplar` → `models/emprestimo_exemplar.py`
- Todas herdam de `Base` (definida em `models/__init__.py`)
- As chaves primárias e estrangeiras foram definidas conforme o modelo relacional da Etapa 1.

### 2. Criar classes de serviço responsáveis pelo CRUD de cada entidade
- Local: Pasta `services/`
- Arquivos:
  - `aluno_service.py`
  - `livro_service.py`
  - `exemplar_service.py`
  - `emprestimo_service.py`
  - `emprestimo_exemplar_service.py`
- Cada serviço contém os métodos:
  - `criar_<entidade>`
  - `listar_<entidade>`
  - `buscar_por_id`
  - `atualizar_<entidade>`
  - `remover_<entidade>`

### 3. Criar o arquivo `db.py` com a configuração de conexão
- Local: `db.py`
- Define a string de conexão usando `psycopg2` com PostgreSQL.
- Cria o `SessionLocal` para ser usado nos serviços.

### 4. Criar um arquivo principal `main.py` para testes
- Local: `main.py`
- Responsável por:
  - Criar um aluno de teste (`teste_criar_aluno()`)
  - Listar alunos cadastrados (`teste_listar_alunos()`)

### 5. Não utilizar `Base.metadata.create_all()`
- Nenhum dos arquivos contém chamadas para criação automática de tabelas.
- O banco deve ser previamente criado no PostgreSQL com base no modelo relacional.

### 6. Usar `session.add()`, `session.commit()`, `session.query()` explicitamente
- Exemplo em `aluno_service.py`:
  ```python
  session = SessionLocal()
  session.add(aluno)
  session.commit()
  session.close()
  ```

- Exemplo de leitura:
  ```python
  alunos = session.query(Aluno).all()
  ```

## Instalação e Uso

### Requisitos
- PostgreSQL instalado localmente
- Python 3.8+
- Banco de dados `biblioteca_db` criado manualmente

### Instalação de dependências
```bash
pip install sqlalchemy psycopg2
```

### Configuração da conexão (arquivo `db.py`)
```python
DATABASE_URL = "postgresql+psycopg2://usuario:senha@localhost:5432/biblioteca_db"
```

### Executando a aplicação
```bash
python biblioteca/main.py
```

## Exemplo da última instrução solicitada no trabalho

Trecho de `main.py` que realiza uma consulta simples de teste:
```python
from db import SessionLocal
from models.aluno import Aluno

session = SessionLocal()

# Exemplo de leitura (consulta)
for aluno in session.query(Aluno).all():
    print(aluno.nome)
```

Este código foi adaptado no `main.py` real para também inserir um aluno e listar todos os alunos da tabela, cumprindo assim completamente a instrução final do roteiro.