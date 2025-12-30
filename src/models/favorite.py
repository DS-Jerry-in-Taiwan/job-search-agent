from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from src.models.database import Base

class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    job_id = Column(String)
    job_title = Column(String)
    company = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
