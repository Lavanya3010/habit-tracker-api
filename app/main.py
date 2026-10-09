
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import Base, engine
from app import models
from app.routers import auth, habits


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Habit Tracker API",
    description="A Habit Tracker API with JWT Authentication and CRUD operations",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(auth.router)
app.include_router(habits.router)


@app.get("/", tags=["Home"])
def home():
    return {
        "message": "Welcome to Habit Tracker API",
        "docs": "/docs"
    }


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}
