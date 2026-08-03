from fastapi import FastAPI
from database import Base, engine
import models

from routers import department
from routers import designation
from routers import city
from routers import employee

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="HR Management API",
    version="1.0"
)

app.include_router(department.router)
app.include_router(designation.router)
app.include_router(city.router)
app.include_router(employee.router)


@app.get("/")
def home():
    return {
        "message": "HR Management API is Running Successfully!"
    }