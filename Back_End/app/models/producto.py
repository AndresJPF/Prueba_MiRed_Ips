from sqlalchemy import (
    Column, BigInteger, String, Text, DECIMAL, Integer,
    Enum, TIMESTAMP, ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Producto(Base):
    __tablename__ = "productos"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    codigo = Column(String(20), nullable=False, unique=True)
    nombre = Column(String(150), nullable=False)
    categoria_id = Column(BigInteger, ForeignKey("categorias.id"), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(DECIMAL(10, 2), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    estado = Column(Enum("activo", "inactivo", name="estado_enum"), nullable=False, default="activo")

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    deleted_at = Column(TIMESTAMP, nullable=True)  # se usa para el soft delete

    # Relación: cada producto pertenece a una categoría
    categoria = relationship("Categoria", back_populates="productos")