from sqlalchemy import Column, Integer, String, Date, ForeignKey
from models import Base

class Emprestimo(Base):
    __tablename__ = "emprestimo"

    id_emprestimo = Column(Integer, primary_key=True)
    matricula_aluno = Column(String, ForeignKey("aluno.matricula"), nullable=False)
    data_emprestimo = Column(Date, nullable=False)
    data_prevista_devolucao = Column(Date, nullable=False)