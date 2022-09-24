from fastapi import FastAPI, Response, status, HTTPException
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

@app.post('/posts', status_code=status.HTTP_201_CREATED)
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
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post {id} not found")
    return {"post selected": post }

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    post_to_delete = find_index_post(id)

    if post_to_delete == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {id} not found")
    my_posts.pop(post_to_delete)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

