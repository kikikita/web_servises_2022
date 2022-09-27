import email
from typing import List

from app.types.order import Order


class User:
    def __init__(self, name: str, email: str, orders: List[Order]) -> None:
        self.name = name
        self.email = email
        self.orders = orders

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, User):
            return False

        user: User = __o

        return self.name == user.name and self.email == user.email and self.orders == user.orders