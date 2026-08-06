from decimal import Decimal
from typing import Optional

from pydantic import BaseModel


class ProductoBase(BaseModel):
    codigo: str
    nombre: str
    categoria_id: int
    descripcion: Optional[str] = None
    precio: Decimal
    stock: int = 0
    estado: Optional[str] = "activo"


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(BaseModel):
    codigo: Optional[str] = None
    nombre: Optional[str] = None
    categoria_id: Optional[int] = None
    descripcion: Optional[str] = None
    precio: Optional[Decimal] = None
    stock: Optional[int] = None
    estado: Optional[str] = None


class ProductoOut(ProductoBase):
    id: int

    class Config:
        from_attributes = True