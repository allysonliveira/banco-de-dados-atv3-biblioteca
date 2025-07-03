from sqlalchemy import Column, Integer, String
from models import Base

class Livro(Base):
    __tablename__ = "livro"

    codigo = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    editora = Column(String, nullable=False)
    ano_publicacao = Column(Integer, nullable=False)