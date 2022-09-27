from typing import List

from app.db import db
from app.types.user import User
from fastapi import APIRouter
from app.product.types import Pizza

product_router = APIRouter(
    prefix='/order',
    tags=['order']
)

@product_router.get('/get-products')
def get_user_products(username: str) -> List[str]:
    user: List[User] = [u for u in db['users'] if u.name == username]

    if not user:
        return []

    products: List[str] = []

    for p in user[0].orders:
        for s in p.products:
            products.append(s)

    return list(set(products))


