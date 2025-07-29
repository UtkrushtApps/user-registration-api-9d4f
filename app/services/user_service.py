from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import UserCreate
from typing import List

async def create_user(db: AsyncSession, user: UserCreate):
    pass

async def list_users(db: AsyncSession):
    pass
