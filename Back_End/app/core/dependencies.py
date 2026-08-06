from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import decode_access_token
from app.models.user import User

# Indica a FastAPI/Swagger dónde se obtiene el token (endpoint de login)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
) -> User:
    """
    Lee el token enviado en el header Authorization, lo valida
    y devuelve el usuario correspondiente. Si algo falla, lanza error 401.
    """
    credenciales_invalidas = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_access_token(token)
    if payload is None:
        raise credenciales_invalidas

    user_id = payload.get("sub")
    if user_id is None:
        raise credenciales_invalidas

    user = db.query(User).filter(
        User.id == int(user_id),
        User.deleted_at.is_(None)
    ).first()

    if user is None:
        raise credenciales_invalidas

    return user


def get_admin_user(current_user: User = Depends(get_current_user)) -> User:
    """Permite el acceso solo si el usuario autenticado tiene rol admin."""
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos de administrador para esta acción"
        )
    return current_user