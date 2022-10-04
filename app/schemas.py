from pydantic import BaseModel

# this class Post comes from the pydantic model. This is our schema.
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = False

class PostCreate(PostBase):
    pass