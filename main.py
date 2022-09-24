from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
{"title": "favourite food", "content": "pizza", "id": 2}]


@app.get('/')
async def root():
    return {'message': 'My FastAPI'}

@app.get('/posts')
def get_posts():
    return {'data': my_posts}

@app.post('/posts')
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 99999999)
    my_posts.append(post_dict)
    return {'data': post_dict}

def find_post(id):
    for post in my_posts:
        if post['id'] == id:
            return post

@app.get('/posts/{id}')
def get_post(id: int):
    post = find_post(id)
    return {"post selected": post }

