from fastapi import FastAPI
from app.api.v1 import users, items, auth

app = FastAPI(
    title="Portfolio Backend API",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(items.router, prefix="/api/v1/items", tags=["items"])

