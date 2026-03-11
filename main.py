from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI instance
app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# Example GET endpoint
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User{user_id}"}

# User model for POST request
class User(BaseModel):
    name: str
    email: str

# Example POST endpoint
@app.post("/users/")
def create_user(user: User):
    return {"message": "User created successfully", "user": user}