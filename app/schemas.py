from datetime import datetime
from pydantic import BaseModel, EmailStr

# these comes from the pydantic model. This is our schema.

# Post shemas
# those handle data coming from the user.
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = False

class PostCreate(PostBase):
    pass


# those handle data back to the user
# Post = PostResponse
class Post(PostBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# User schemas

class UserBase(BaseModel):
    # name: str
    email: EmailStr


# those handle data coming from the user.
class UserCreate(UserBase):
    password: str


# those handle data back to the user
class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# login schemas
class UserLogin(UserBase):
    password: str