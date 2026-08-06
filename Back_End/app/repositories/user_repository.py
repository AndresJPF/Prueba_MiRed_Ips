from datetime import datetime

from sqlalchemy.orm import Session

from app.models.user import User


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(User)
        .filter(User.deleted_at.is_(None))
        .offset(skip)
        .limit(limit)
        .all()
    )


def count_users(db: Session):
    return db.query(User).filter(User.deleted_at.is_(None)).count()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(
        User.id == user_id,
        User.deleted_at.is_(None)
    ).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(
        User.email == email,
        User.deleted_at.is_(None)
    ).first()


def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user(db: Session, user: User):
    db.commit()
    db.refresh(user)
    return user


def delete_user(db: Session, user: User):
    # Soft delete: solo se marca la fecha de eliminación
    user.deleted_at = datetime.utcnow()
    db.commit()
    return user