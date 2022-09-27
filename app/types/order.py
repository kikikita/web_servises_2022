from typing import List


class Order:
    def __init__(self, adress: str, products: List[str]) -> None:
        self.adress = adress
        self.products = products

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Order):
            return False

        order: Order = __o

        return self.adress == order.adress and self.products == order.products