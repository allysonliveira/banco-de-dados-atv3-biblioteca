from sqlalchemy import Column, Integer, Date, ForeignKey
from models import Base

class EmprestimoExemplar(Base):
    __tablename__ = "itememprestimo"

    id_emprestimo = Column(Integer, ForeignKey("emprestimo.id_emprestimo"), primary_key=True)
    tombo_exemplar = Column(Integer, ForeignKey("exemplar.tombo"), primary_key=True)
    data_devolucao = Column(Date, nullable=True)
    dias_atraso = Column(Integer, nullable=True)