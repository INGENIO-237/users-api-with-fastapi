from fastapi import APIRouter, HTTPException

from models.users import UpdateUser, User
from schemas.users import usersSchema

from config.db import db

user = APIRouter()

@user.get('/')
async def home():
    return {'Hello': "Dunya"}

@user.get('/api/v1/users')
async def users():
    return usersSchema(db.fastapi.users.find())

@user.post('/api/v1/users')
async def add_user(user: User):
    try:
        user = db.fastapi.users.insert_one(dict(user))
        user = db.fastapi.users.find_one(user.inserted_id)
        return usersSchema(user)
    except Exception as e:
        raise e

@user.delete('/api/v1/users/{id: str}')
async def delete_user(id: str):
    raise HTTPException(
        status_code=404,
        detail=f'The user with id ({id}) doesn\'t exist'
    )

@user.put('/api/v1/users/{id: str}')
async def update_user(id: str, update_user: UpdateUser):
    raise HTTPException(
        status_code=404, 
        detail=f'The user with id ({id}) doesn\'t exist'
    )