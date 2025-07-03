from models.emprestimo import Emprestimo
from db import SessionLocal

def criar_emprestimo(emprestimo: Emprestimo):
    session = SessionLocal()
    session.add(emprestimo)
    session.commit()
    session.close()

def listar_emprestimos():
    session = SessionLocal()
    emprestimos = session.query(Emprestimo).all()
    session.close()
    return emprestimos

def buscar_por_id(id_emprestimo: int):
    session = SessionLocal()
    emprestimo = session.query(Emprestimo).filter_by(id_emprestimo=id_emprestimo).first()
    session.close()
    return emprestimo

def atualizar_emprestimo(id_emprestimo: int, novos_dados: dict):
    session = SessionLocal()
    emprestimo = session.query(Emprestimo).filter_by(id_emprestimo=id_emprestimo).first()
    if emprestimo:
        for chave, valor in novos_dados.items():
            setattr(emprestimo, chave, valor)
        session.commit()
    session.close()

def remover_emprestimo(id_emprestimo: int):
    session = SessionLocal()
    emprestimo = session.query(Emprestimo).filter_by(id_emprestimo=id_emprestimo).first()
    if emprestimo:
        session.delete(emprestimo)
        session.commit()
    session.close()