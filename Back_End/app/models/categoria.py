from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.core.database import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text, nullable=True)

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    # Relación: una categoría puede tener muchos productos
    productos = relationship("Producto", back_populates="categoria")