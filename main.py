from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'My FastAPI'}

@app.get('/posts')
def get_posts():
    return {'data': 'All posts'}

@app.post('/createpost')
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return {'new_post': f"Title: {payLoad['title']} Content: {payLoad['content']}"}
