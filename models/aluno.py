from sqlalchemy import Column, String
from models import Base

class Aluno(Base):
    __tablename__ = "aluno"

    matricula = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    curso = Column(String, nullable=False)