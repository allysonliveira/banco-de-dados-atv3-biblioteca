from db import SessionLocal
from models.aluno import Aluno
from services import aluno_service

def teste_criar_aluno():
    novo_aluno = Aluno(
        matricula="2023123456",
        nome="Maria Silva",
        email="maria.silva@example.com",
        curso="Engenharia da Computação"
    )
    aluno_service.criar_aluno(novo_aluno)

def teste_listar_alunos():
    alunos = aluno_service.listar_alunos()
    for aluno in alunos:
        print(f"{aluno.matricula} - {aluno.nome} - {aluno.email} - {aluno.curso}")

if __name__ == "__main__":
    print("Testando criação e listagem de alunos:")
    teste_criar_aluno()
    teste_listar_alunos()