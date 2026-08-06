from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.producto import Producto
from app.repositories import categoria_repository, producto_repository
from app.schemas.producto import ProductoCreate, ProductoUpdate


def list_productos(
    db: Session,
    page: int = 1,
    page_size: int = 10,
    categoria_id: Optional[int] = None,
    estado: Optional[str] = None
):
    skip = (page - 1) * page_size
    productos = producto_repository.get_productos(
        db, skip=skip, limit=page_size, categoria_id=categoria_id, estado=estado
    )
    total = producto_repository.count_productos(db, categoria_id=categoria_id, estado=estado)
    return productos, total


def get_producto(db: Session, producto_id: int):
    producto = producto_repository.get_producto_by_id(db, producto_id)
    if not producto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return producto


def create_producto(db: Session, data: ProductoCreate):
    producto_existente = producto_repository.get_producto_by_codigo(db, data.codigo)
    if producto_existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El código de producto ya existe")

    categoria = categoria_repository.get_categoria_by_id(db, data.categoria_id)
    if not categoria:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La categoría indicada no existe")

    nuevo_producto = Producto(**data.dict())
    return producto_repository.create_producto(db, nuevo_producto)


def update_producto(db: Session, producto_id: int, data: ProductoUpdate):
    producto = get_producto(db, producto_id)

    if data.codigo and data.codigo != producto.codigo:
        producto_existente = producto_repository.get_producto_by_codigo(db, data.codigo)
        if producto_existente:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El código de producto ya existe")
        producto.codigo = data.codigo

    if data.categoria_id:
        categoria = categoria_repository.get_categoria_by_id(db, data.categoria_id)
        if not categoria:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La categoría indicada no existe")
        producto.categoria_id = data.categoria_id

    if data.nombre:
        producto.nombre = data.nombre

    if data.descripcion is not None:
        producto.descripcion = data.descripcion

    if data.precio is not None:
        producto.precio = data.precio

    if data.stock is not None:
        producto.stock = data.stock

    if data.estado:
        producto.estado = data.estado

    return producto_repository.update_producto(db, producto)


def delete_producto(db: Session, producto_id: int):
    producto = get_producto(db, producto_id)
    return producto_repository.delete_producto(db, producto)