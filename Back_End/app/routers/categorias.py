from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.models.categoria import Categoria
from app.repositories import categoria_repository
from app.schemas.categoria import CategoriaCreate, CategoriaOut, CategoriaUpdate

# Todas las rutas de este router requieren usuario autenticado
router = APIRouter(prefix="/categorias", tags=["Categorías"], dependencies=[Depends(get_current_user)])


@router.get("/", response_model=List[CategoriaOut])
def list_categorias(db: Session = Depends(get_db)):
    """Lista todas las categorías disponibles."""
    return categoria_repository.get_categorias(db)


@router.get("/{categoria_id}", response_model=CategoriaOut)
def get_categoria(categoria_id: int, db: Session = Depends(get_db)):
    """Obtiene el detalle de una categoría por su id."""
    categoria = categoria_repository.get_categoria_by_id(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")
    return categoria


@router.post("/", response_model=CategoriaOut, status_code=201)
def create_categoria(data: CategoriaCreate, db: Session = Depends(get_db)):
    """Crea una nueva categoría."""
    existente = categoria_repository.get_categoria_by_nombre(db, data.nombre)
    if existente:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ya existe una categoría con ese nombre")

    nueva_categoria = Categoria(**data.dict())
    return categoria_repository.create_categoria(db, nueva_categoria)


@router.put("/{categoria_id}", response_model=CategoriaOut)
def update_categoria(categoria_id: int, data: CategoriaUpdate, db: Session = Depends(get_db)):
    """Actualiza una categoría existente."""
    categoria = categoria_repository.get_categoria_by_id(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")

    if data.nombre:
        categoria.nombre = data.nombre
    if data.descripcion is not None:
        categoria.descripcion = data.descripcion

    return categoria_repository.update_categoria(db, categoria)


@router.delete("/{categoria_id}", status_code=204)
def delete_categoria(categoria_id: int, db: Session = Depends(get_db)):
    """Elimina una categoría."""
    categoria = categoria_repository.get_categoria_by_id(db, categoria_id)
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada")

    categoria_repository.delete_categoria(db, categoria)
    return None