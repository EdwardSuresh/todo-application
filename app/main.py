from fastapi import FastAPI

from .database import engine, Base
from .routes.todos import router as todos_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API for Python using FASTAPI and SQLAlchemy", version="1.0.0")

app.include_router(todos_router)

