from datetime import datetime
from turtle import title
from pydantic import BaseModel

# this class Post comes from the pydantic model. This is our schema.
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
