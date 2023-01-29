from typing import List
from models.users import User


def userSchema(user: User):
    return {
        'id': str(user['_id']),
        'firstname': user['firstname'],
        'lastname': user['lastname'],
        'gender': user['gender'],
        'roles': user['roles'],
    }

def usersSchema(users: List[User]):
    return [userSchema(user) for user in users]