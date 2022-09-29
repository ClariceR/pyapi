from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
import psycopg2
from dotenv import dotenv_values

config = dotenv_values(".env")
host = config['HOST']
database = config['DATABASE']
user = config['USER']
password = config['PASSWORD']

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    is_published: bool = False

try:
    conn = psycopg2.connect(host=host, database=database, user=user, password=password)
    cursor = conn.cursor()
except Exception as error:
    print('Could not connect to database')
    print('Error: ', error)

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, 
{"title": "favourite food", "content": "pizza", "id": 2}]


@app.get('/')
async def root():
    return {'message': 'My FastAPI'}

@app.get('/posts')
def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {'data': posts}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, is_published) VALUES (%s, %s, %s) RETURNING *""", (post.title, post.content, post.is_published))
    new_post = cursor.fetchone()
    conn.commit()

    return {'data': new_post}

# def find_post(id):
#     for post in my_posts:
#         if post['id'] == id:
#             return post

@app.get('/posts/{id}')
def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s""", [str(id)])
    post = cursor.fetchone()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post {id} not found")
    return {"post_selected": post }



@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
  
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post {id} not found")
    conn.commit()
  
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put('/posts/{id}')
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title = %s, content = %s WHERE id = %s RETURNING *""", (post.title, post.content, str(id)))
    post = cursor.fetchone()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post {id} not found")
    
    conn.commit()
    return {"data": post}

