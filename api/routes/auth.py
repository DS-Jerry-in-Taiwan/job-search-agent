from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from src.auth.auth_service import register_user, authenticate_user, get_user_by_id
from src.auth.jwt_handler import create_access_token, verify_token
from src.auth.password_handler import verify_password
from src.models.user import User

router = APIRouter()

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

@router.post("/register")
def register(data: UserRegister):
    try:
        user = register_user(data.email, data.password, data.full_name)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    token = create_access_token(user.id)
    return {"user_id": user.id, "email": user.email, "access_token": token}

@router.post("/login")
def login(data: UserLogin):
    try:
        user = authenticate_user(data.email, data.password)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(user.id)
    return {"access_token": token, "token_type": "bearer"}

@router.get("/me")
def me(token: str):
    try:
        user_id = verify_token(token)
    except:
        raise HTTPException(status_code=401, detail="Invalid token")
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
