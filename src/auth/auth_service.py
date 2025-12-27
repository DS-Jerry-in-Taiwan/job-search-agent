from src.models.database import SessionLocal
from src.models.user import User
from src.auth.password_handler import hash_password, verify_password
from sqlalchemy.orm import Session
from typing import Optional

def register_user(email: str, password: str, full_name: str) -> User:
    db: Session = SessionLocal()
    user = User(email=email, hashed_password=hash_password(password), full_name=full_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user

def authenticate_user(email: str, password: str) -> Optional[User]:
    db: Session = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    db.close()
    if user and verify_password(password, user.hashed_password):
        return user
    return None

def get_user_by_id(user_id: int) -> Optional[User]:
    db: Session = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    return user

def get_user_by_email(email: str) -> Optional[User]:
    db: Session = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    db.close()
    return user
