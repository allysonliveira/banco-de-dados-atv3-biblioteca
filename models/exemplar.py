from sqlalchemy import Column, Integer, ForeignKey
from models import Base

class Exemplar(Base):
    __tablename__ = "exemplar"

    tombo = Column(Integer, primary_key=True)
    codigo_livro = Column(Integer, ForeignKey("livro.codigo"), nullable=False)