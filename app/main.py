# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Instrumentation for Prometheus
Instrumentator().instrument(app).expose(app)

class User(BaseModel):
    username: str
    email: str

@app.get("/status")
def get_status():
    return {"status": "OK", "message": "API is running"}

@app.post("/register")
def register_user(user: User):
    return {"message": f"User {user.username} registered with email {user.email}"}
