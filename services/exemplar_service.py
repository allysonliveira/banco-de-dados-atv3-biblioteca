from models.exemplar import Exemplar
from db import SessionLocal

def criar_exemplar(exemplar: Exemplar):
    session = SessionLocal()
    session.add(exemplar)
    session.commit()
    session.close()

def listar_exemplares():
    session = SessionLocal()
    exemplares = session.query(Exemplar).all()
    session.close()
    return exemplares

def buscar_por_id(tombo: int):
    session = SessionLocal()
    exemplar = session.query(Exemplar).filter_by(tombo=tombo).first()
    session.close()
    return exemplar

def atualizar_exemplar(tombo: int, novos_dados: dict):
    session = SessionLocal()
    exemplar = session.query(Exemplar).filter_by(tombo=tombo).first()
    if exemplar:
        for chave, valor in novos_dados.items():
            setattr(exemplar, chave, valor)
        session.commit()
    session.close()

def remover_exemplar(tombo: int):
    session = SessionLocal()
    exemplar = session.query(Exemplar).filter_by(tombo=tombo).first()
    if exemplar:
        session.delete(exemplar)
        session.commit()
    session.close()