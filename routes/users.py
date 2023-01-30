from fastapi import APIRouter, HTTPException

from models.users import UpdateUser, User
from schemas.users import userSchema, usersSchema

from config.db import db

user = APIRouter()

# Home endpoint
@user.get('/')
async def home():
    return {'Hello': "Dunya"}

# Get users
@user.get('/api/v1/users')
async def users():
    return usersSchema(db.fastapi.users.find())

# Get user
@user.get('/api/v1/users/{id: str}')
async def find_user(id: str):
    user =  db.fastapi.users.find_one({'_id': id})

# Create user
@user.post('/api/v1/users')
async def add_user(user: User):
    try:
        user = db.fastapi.users.insert_one(dict(user))
        user = db.fastapi.users.find_one(user.inserted_id)
        return usersSchema(user)
    except Exception as e:
        raise e

# Delete user
@user.delete('/api/v1/users/{id: str}')
async def delete_user(id: str):
    try:
        db.fastapi.users.find_one_and_delete({'_id': id})
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise e

# Modify user
@user.put('/api/v1/users/{id: str}')
async def update_user(id: str, update_user: UpdateUser):
    try:
        user = db.fastapi.users.find_one_and_update({'_id': id}, dict(update_user))
        return userSchema(user)
    except Exception as e:
        raise e