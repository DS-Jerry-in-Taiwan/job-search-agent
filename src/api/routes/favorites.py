from fastapi import APIRouter, HTTPException
from src.auth.jwt_handler import verify_token
from src.models.favorite import Favorite
from src.models.database import SessionLocal

router = APIRouter()

@router.get("/")
def get_favorites(token: str):
    user_id = verify_token(token)
    db = SessionLocal()
    favorites = db.query(Favorite).filter(Favorite.user_id == user_id).all()
    db.close()
    return [
        {
            "id": f.id,
            "job_id": f.job_id,
            "job_title": f.job_title,
            "company": f.company,
            "created_at": f.created_at
        }
        for f in favorites
    ]

@router.post("/")
def add_favorite(token: str, job_id: str, job_title: str, company: str):
    user_id = verify_token(token)
    db = SessionLocal()
    exists = db.query(Favorite).filter(Favorite.user_id == user_id, Favorite.job_id == job_id).first()
    if exists:
        db.close()
        raise HTTPException(status_code=400, detail="Already favorited")
    favorite = Favorite(user_id=user_id, job_id=job_id, job_title=job_title, company=company)
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    db.close()
    return {"message": "收藏成功"}

@router.delete("/{job_id}")
def remove_favorite(token: str, job_id: str):
    user_id = verify_token(token)
    db = SessionLocal()
    favorite = db.query(Favorite).filter(Favorite.user_id == user_id, Favorite.job_id == job_id).first()
    if not favorite:
        db.close()
        raise HTTPException(status_code=404, detail="Favorite not found")
    db.delete(favorite)
    db.commit()
    db.close()
    return {"message": "取消收藏成功"}
