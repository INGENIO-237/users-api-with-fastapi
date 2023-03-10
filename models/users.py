from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"

class User(BaseModel):
    firstname: str
    lastname: Optional[str]
    gender: Gender
    roles: List[Role]

class UpdateUser(BaseModel):
    firstname: Optional[str]
    lastname: Optional[str]
    gender: Optional[Gender]
    roles: Optional[List[Role]]
