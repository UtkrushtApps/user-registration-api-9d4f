from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import UserCreate, UserOut
from app.services.user_service import create_user, list_users
from app.db.session import get_db
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    pass

@router.get("/", response_model=List[UserOut])
async def get_users(db: AsyncSession = Depends(get_db)):
    pass
