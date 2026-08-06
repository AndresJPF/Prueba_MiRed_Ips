from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.models.user import User
from app.repositories import user_repository
from app.schemas.auth import LoginRequest, RegisterRequest


def register_user(db: Session, data: RegisterRequest):
    usuario_existente = user_repository.get_user_by_email(db, data.email)
    if usuario_existente:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un usuario registrado con ese correo"
        )

    nuevo_usuario = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
        role="empleado"
    )

    return user_repository.create_user(db, nuevo_usuario)


def login_user(db: Session, data: LoginRequest) -> str:
    usuario = user_repository.get_user_by_email(db, data.email)

    if not usuario or not verify_password(data.password, usuario.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Correo o contraseña incorrectos"
        )

    access_token = create_access_token(data={"sub": str(usuario.id)})
    return access_token