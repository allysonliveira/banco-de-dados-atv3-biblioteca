from models.livro import Livro
from db import SessionLocal

def criar_livro(livro: Livro):
    session = SessionLocal()
    session.add(livro)
    session.commit()
    session.close()

def listar_livros():
    session = SessionLocal()
    livros = session.query(Livro).all()
    session.close()
    return livros

def buscar_por_id(codigo: int):
    session = SessionLocal()
    livro = session.query(Livro).filter_by(codigo=codigo).first()
    session.close()
    return livro

def atualizar_livro(codigo: int, novos_dados: dict):
    session = SessionLocal()
    livro = session.query(Livro).filter_by(codigo=codigo).first()
    if livro:
        for chave, valor in novos_dados.items():
            setattr(livro, chave, valor)
        session.commit()
    session.close()

def remover_livro(codigo: int):
    session = SessionLocal()
    livro = session.query(Livro).filter_by(codigo=codigo).first()
    if livro:
        session.delete(livro)
        session.commit()
    session.close()