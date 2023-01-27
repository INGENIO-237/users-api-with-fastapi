from typing import List
from fastapi import FastAPI

from models import Gender, Role, User

app = FastAPI()

db: List[User] = [
    User(firstname='John', gender=Gender.male, roles=[Role.user]),
    User(firstname='Doe', gender=Gender.male, roles=[Role.admin]),
]

@app.get('/')
def home():
    return {"Hello": "Mundo"}