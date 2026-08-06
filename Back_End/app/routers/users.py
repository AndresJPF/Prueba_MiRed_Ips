from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.schemas.user import UserCreate, UserOut, UserUpdate
from app.services import user_service

# Todas las rutas de este router requieren usuario autenticado
router = APIRouter(prefix="/users", tags=["Usuarios"], dependencies=[Depends(get_current_user)])


@router.get("/")
def list_users(
    page: int = Query(1, ge=1, description="Número de página"),
    page_size: int = Query(10, ge=1, le=100, description="Cantidad de registros por página"),
    db: Session = Depends(get_db)
):
    """Lista los usuarios de forma paginada."""
    usuarios, total = user_service.list_users(db, page, page_size)
    return {
        "data": [UserOut.model_validate(u) for u in usuarios],
        "total": total,
        "page": page,
        "page_size": page_size
    }


@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Obtiene el detalle de un usuario por su id."""
    return user_service.get_user(db, user_id)


@router.post("/", response_model=UserOut, status_code=201)
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    """Crea un nuevo usuario."""
    return user_service.create_user(db, data)


@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    """Actualiza los datos de un usuario existente."""
    return user_service.update_user(db, user_id, data)


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Elimina (soft delete) un usuario."""
    user_service.delete_user(db, user_id)
    return None