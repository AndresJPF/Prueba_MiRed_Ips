from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Session

from app.models.producto import Producto


def get_productos(
    db: Session,
    skip: int = 0,
    limit: int = 10,
    categoria_id: Optional[int] = None,
    estado: Optional[str] = None
):
    query = db.query(Producto).filter(Producto.deleted_at.is_(None))

    if categoria_id is not None:
        query = query.filter(Producto.categoria_id == categoria_id)

    if estado is not None:
        query = query.filter(Producto.estado == estado)

    return query.offset(skip).limit(limit).all()


def count_productos(
    db: Session,
    categoria_id: Optional[int] = None,
    estado: Optional[str] = None
):
    query = db.query(Producto).filter(Producto.deleted_at.is_(None))

    if categoria_id is not None:
        query = query.filter(Producto.categoria_id == categoria_id)

    if estado is not None:
        query = query.filter(Producto.estado == estado)

    return query.count()


def get_producto_by_id(db: Session, producto_id: int):
    return db.query(Producto).filter(
        Producto.id == producto_id,
        Producto.deleted_at.is_(None)
    ).first()


def get_producto_by_codigo(db: Session, codigo: str):
    return db.query(Producto).filter(
        Producto.codigo == codigo,
        Producto.deleted_at.is_(None)
    ).first()


def create_producto(db: Session, producto: Producto):
    db.add(producto)
    db.commit()
    db.refresh(producto)
    return producto


def update_producto(db: Session, producto: Producto):
    db.commit()
    db.refresh(producto)
    return producto


def delete_producto(db: Session, producto: Producto):
    # Soft delete: solo se marca la fecha de eliminación
    producto.deleted_at = datetime.utcnow()
    db.commit()
    return producto