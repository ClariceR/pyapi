import psycopg2
from fastapi import FastAPI

from . import models
from .database import engine
from .routers import post, user, auth


from dotenv import dotenv_values

config = dotenv_values(".env")
host = config['HOST']
database = config['DATABASE']
db_user = config['USER']
password = config['PASSWORD']


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

try:
    conn = psycopg2.connect(host=host, database=database, user=db_user, password=password)
    cursor = conn.cursor()
except Exception as error:
    print('Could not connect to database')
    print('Error: ', error)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get('/')
async def root():
    return {'message': 'My FastAPI'}

