from sqlalchemy.orm import Session

from app.models.categoria import Categoria


def get_categorias(db: Session):
    return db.query(Categoria).all()


def get_categoria_by_id(db: Session, categoria_id: int):
    return db.query(Categoria).filter(Categoria.id == categoria_id).first()


def get_categoria_by_nombre(db: Session, nombre: str):
    return db.query(Categoria).filter(Categoria.nombre == nombre).first()


def create_categoria(db: Session, categoria: Categoria):
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria


def update_categoria(db: Session, categoria: Categoria):
    db.commit()
    db.refresh(categoria)
    return categoria


def delete_categoria(db: Session, categoria: Categoria):
    # La tabla categorias no tiene soft delete en el esquema, se elimina físicamente
    db.delete(categoria)
    db.commit()