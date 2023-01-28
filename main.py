from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException

from models import Gender, Role, UpdateUser, User

app = FastAPI()

db: List[User] = [
    User(firstname='John', gender=Gender.male, roles=[Role.user]),
    User(firstname='Doe', gender=Gender.male, roles=[Role.admin]),
]

@app.get('/')
async def home():
    return {'Hello': "Mundo"}

@app.get('/api/v1/users')
async def users():
    return db

@app.post('/api/v1/users')
async def add_user(user: User):
    db.append(user)
    return {'user': user}

@app.delete('/api/v1/users/{id: UUID}')
async def delete_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f'The user with id ({id}) doesn\'t exist'
    )

@app.put('/api/v1/users/{id: UUID}')
async def update_user(id: UUID, update_user: UpdateUser):
    for user in db:
        if user.id == id:
            if update_user.firstname is not None:
                user.firstname = update_user.firstname
            if update_user.lastname is not None:
                user.lastname = update_user.lastname
            if update_user.gender is not None:
                user.gender = update_user.gender
            if update_user.roles is not None:
                for role in update_user.roles:
                    if role not in user.roles:
                        user.roles.append(role)
            return {'user': user}
    raise HTTPException(
        status_code=404, 
        detail=f'The user with id ({id}) doesn\'t exist'
    )