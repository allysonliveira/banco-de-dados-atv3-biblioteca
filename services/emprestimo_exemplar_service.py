from models.emprestimo_exemplar import EmprestimoExemplar
from db import SessionLocal

def adicionar_exemplar_ao_emprestimo(item: EmprestimoExemplar):
    session = SessionLocal()
    session.add(item)
    session.commit()
    session.close()

def listar_itens_emprestimo():
    session = SessionLocal()
    itens = session.query(EmprestimoExemplar).all()
    session.close()
    return itens

def buscar_por_id(id_emprestimo: int, tombo_exemplar: int):
    session = SessionLocal()
    item = session.query(EmprestimoExemplar).filter_by(
        id_emprestimo=id_emprestimo, tombo_exemplar=tombo_exemplar
    ).first()
    session.close()
    return item

def atualizar_item_emprestimo(id_emprestimo: int, tombo_exemplar: int, novos_dados: dict):
    session = SessionLocal()
    item = session.query(EmprestimoExemplar).filter_by(
        id_emprestimo=id_emprestimo, tombo_exemplar=tombo_exemplar
    ).first()
    if item:
        for chave, valor in novos_dados.items():
            setattr(item, chave, valor)
        session.commit()
    session.close()

def remover_item_emprestimo(id_emprestimo: int, tombo_exemplar: int):
    session = SessionLocal()
    item = session.query(EmprestimoExemplar).filter_by(
        id_emprestimo=id_emprestimo, tombo_exemplar=tombo_exemplar
    ).first()
    if item:
        session.delete(item)
        session.commit()
    session.close()