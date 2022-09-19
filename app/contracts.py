from pydantic import BaseModel


class Item(BaseModel):
    """Contract for item."""

    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    