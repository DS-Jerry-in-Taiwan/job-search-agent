from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from src.auth.jwt_handler import verify_token
from src.auth.auth_service import get_user_by_id
from src.models.user import User
from src.models.search_history import SearchHistory
from src.models.database import SessionLocal
from typing import List

router = APIRouter()

class UserProfileUpdate(BaseModel):
    full_name: str
    skills: list[str] = []
    preferences: dict = {}

@router.get("/profile")
def get_profile(token: str):
    user_id = verify_token(token)
    user = get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "skills": user.skills,
        "preferences": user.preferences
    }

@router.put("/profile")
def update_profile(token: str, data: UserProfileUpdate):
    user_id = verify_token(token)
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        db.close()
        raise HTTPException(status_code=404, detail="User not found")
    user.full_name = data.full_name
    user.skills = data.skills
    user.preferences = data.preferences
    db.commit()
    db.refresh(user)
    db.close()
    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "skills": user.skills,
        "preferences": user.preferences
    }

@router.get("/history")
def get_history(token: str, limit: int = 20, offset: int = 0):
    user_id = verify_token(token)
    db = SessionLocal()
    history = db.query(SearchHistory).filter(SearchHistory.user_id == user_id).order_by(SearchHistory.created_at.desc()).offset(offset).limit(limit).all()
    db.close()
    return [
        {
            "id": h.id,
            "query": h.query,
            "filters": h.filters,
            "results_count": h.results_count,
            "created_at": h.created_at
        }
        for h in history
    ]
