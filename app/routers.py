from fastapi import APIRouter

from app import contracts

router = APIRouter()


@router.get("/")
def read_root():  # noqa: D103
    return {"Hello": "World"}
    
@router.get("/a")
def read_root():  # noqa: D103
    return {"Hello": "AAAA"}

@router.get("/items/{item_id}")
async def read_item(item_id: int):  # noqa: D103
    return {"item_id": item_id}


@router.get("/users/")
async def read_user(user_id: str, q: str | None = None):
    if q:
        return {"item_id": user_id, "q": q}
    return {"item_id": user_id}


@router.get("/users/{user_id}/items/{item_id}")
async def read_user_item(  # noqa: D103
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@router.post("/items/")
async def create_item(item: contracts.Item):  # noqa: D103
    item_dict = item.dict()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
    