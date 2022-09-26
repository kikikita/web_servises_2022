from fastapi import APIRouter

menu_router=APIRouter(
    prefix='/menu',
    tags=['menu']
)


@menu_router.get('/')
async def hello():
    return{'Hello':'World'}  