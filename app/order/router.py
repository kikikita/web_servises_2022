from typing import List, Optional

from app.db import db
from app.order.types import Order
from app.types.order import Order as OrderModel
from app.types.user import User
from fastapi import APIRouter

order_router = APIRouter(
    prefix='/order',
    tags=['order']
)


@order_router.get('/get-adress')
def user_adress(username: str) -> List[str]:
    user: Optional[User] = next(
        (u for u in db['users'] if u.name == username), None)

    if not user:
        return []

    return [order.adress for order in user.orders]


@order_router.post('/add')
def add_order(order: Order) -> None:
    user: User = next(
        (u for u in db['users'] if u.name == order.username), None)

    if user:
        idx = db['users'].index(user)
        db['users'][idx].orders.append(
            OrderModel(order.adress, order.products)
        )