# app/main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Sample user model
class User(BaseModel):
    username: str
    email: str

@app.get("/status")
def get_status():
    return {"status": "OK", "message": "API is running"}

@app.post("/register")
def register_user(user: User):
    return {"message": f"User {user.username} registered with email {user.email}"}
