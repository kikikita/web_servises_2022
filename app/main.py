from fastapi import FastAPI
from app.auth.auth_routes import auth_router
from app.orders.order_routes import order_router
from app.menu.menu_routes import menu_router

app = FastAPI(    
    title="BaseApp",
    description=("BaseApp"),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/docs/redoc",)

app.include_router(auth_router)
app.include_router(order_router)
app.include_router(menu_router)
