from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
 
from app.core.config import settings
 
# Motor de conexión a la base de datos
engine = create_engine(settings.DATABASE_URL)
 
# Fábrica de sesiones para hablar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
# Clase base de la que heredan todos los modelos
Base = declarative_base()
 
 
def get_db():
    """
    Dependencia de FastAPI que abre una sesión de base de datos
    y la cierra automáticamente al terminar la petición.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()