from models.aluno import Aluno
from db import SessionLocal

def criar_aluno(aluno: Aluno):
    session = SessionLocal()
    session.add(aluno)
    session.commit()
    session.close()

def listar_alunos():
    session = SessionLocal()
    alunos = session.query(Aluno).all()
    session.close()
    return alunos

def buscar_por_id(matricula: str):
    session = SessionLocal()
    aluno = session.query(Aluno).filter_by(matricula=matricula).first()
    session.close()
    return aluno

def atualizar_aluno(matricula: str, novos_dados: dict):
    session = SessionLocal()
    aluno = session.query(Aluno).filter_by(matricula=matricula).first()
    if aluno:
        for chave, valor in novos_dados.items():
            setattr(aluno, chave, valor)
        session.commit()
    session.close()

def remover_aluno(matricula: str):
    session = SessionLocal()
    aluno = session.query(Aluno).filter_by(matricula=matricula).first()
    if aluno:
        session.delete(aluno)
        session.commit()
    session.close()