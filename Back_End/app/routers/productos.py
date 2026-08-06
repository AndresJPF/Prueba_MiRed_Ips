from typing import List

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.schemas.producto import ProductoCreate, ProductoOut, ProductoUpdate
from app.services import producto_service

# Todas las rutas de este router requieren usuario autenticado
router = APIRouter(prefix="/productos", tags=["Productos"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=List[ProductoOut])
def list_productos(
    page: int = Query(1, ge=1, description="Número de página"),
    page_size: int = Query(10, ge=1, le=100, description="Cantidad de registros por página"),
    categoria_id: int | None = Query(None, description="Filtrar por categoría"),
    estado: str | None = Query(None, description="Filtrar por estado"),
    db: Session = Depends(get_db),
):
    """Lista los productos de forma paginada."""
    productos, total = producto_service.list_productos(
        db,
        page=page,
        page_size=page_size,
        categoria_id=categoria_id,
        estado=estado,
    )
    return {
        "data": [ProductoOut.model_validate(p) for p in productos],
        "total": total,
        "page": page,
        "page_size": page_size,
    }


@router.get("/{producto_id}", response_model=ProductoOut)
def get_producto(producto_id: int, db: Session = Depends(get_db)):
    """Obtiene el detalle de un producto por su id."""
    return producto_service.get_producto(db, producto_id)


@router.post("/", response_model=ProductoOut, status_code=201)
def create_producto(data: ProductoCreate, db: Session = Depends(get_db)):
    """Crea un nuevo producto."""
    return producto_service.create_producto(db, data)


@router.put("/{producto_id}", response_model=ProductoOut)
def update_producto(producto_id: int, data: ProductoUpdate, db: Session = Depends(get_db)):
    """Actualiza un producto existente."""
    return producto_service.update_producto(db, producto_id, data)


@router.delete("/{producto_id}", status_code=204)
def delete_producto(producto_id: int, db: Session = Depends(get_db)):
    """Elimina (soft delete) un producto."""
    producto_service.delete_producto(db, producto_id)
    return None
