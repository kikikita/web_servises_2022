from typing import List, Optional

from app.auth.types import User
from app.db import db
from app.types.user import User as UserModel
from fastapi import APIRouter

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/register')
def register(user: User) -> None:
    user_from_db: Optional[UserModel] = next(
        (u for u in db['users'] if u.name == user.name), None)

    if not user_from_db:
        db['users'].append(UserModel(user.name, user.email, []))


@router.get('/list')
def users_list() -> List[UserModel]:
    return db['users']

