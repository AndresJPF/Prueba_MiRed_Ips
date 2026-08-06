from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.dependencies import get_current_user
from app.schemas.auth import LoginRequest, RegisterRequest, Token
from app.schemas.user import UserOut
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Autenticación"])


@router.post("/register", response_model=UserOut, status_code=201)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    """Registra un nuevo usuario en el sistema."""
    return auth_service.register_user(db, data)


@router.post("/login", response_model=Token)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    """Inicia sesión y devuelve un token de acceso (JWT)."""
    access_token = auth_service.login_user(db, data)
    return Token(access_token=access_token)


@router.post("/logout")
def logout(current_user=Depends(get_current_user)):
    """
    Cierra la sesión. Como se usa JWT (sin estado en el servidor),
    basta con que el cliente elimine el token que tiene guardado.
    """
    return {"message": "Sesión cerrada correctamente"}


@router.get("/me", response_model=UserOut)
def me(current_user=Depends(get_current_user)):
    """Devuelve los datos del usuario autenticado."""
    return current_user