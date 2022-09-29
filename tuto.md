## Set up virtual environment
Inside the project folder:
```
    python3 -m venv <name>
```
Make sure the editor updates the interpreter, or update it yourself
To enter the virtual environment in the terminal:
```
    source venv/bin/activate
```
Now we install fastapi inside the venv:
```
    pip install "fastapi[all]"
```
In our main folder:
1. import FastAPI (Python class that provides all the functionality for your API.)
2. create a FastAPI instance (This will be the main point of interaction to create all your API.)
3. create a path opertation ("Path" here refers to the last part of the URL starting from the first /. And "Operation" here refers to one of the HTTP "methods".)
Define a path operation decorator
4. define the path operation function
5. return the content

```python
from fastapi import FastAPI

app = FatsAPI()

@app.get("/")
async def root():
    return {"message": "Hello, world!"}
```

To start the server:
```
    uvicorn main:app --reload
```
main is the file to run
app is the FastAPI instance
--reload automatically restarts the server to reflect the changes in the code

When we create something, we should send a 201 response
When something doesn't exist, we should send a 404 response
when we delete something, we should send a 204 response. We also don't send any data back, but we can return a 204 status
To change the default status, we pass another option to the decorator


## Optional property
If you want to have a property for your Post object that is optional:
```python
from typing import Optional
class Post(BaseModel):
    rating: Optional[int] = None
```

## Setting up .env file
1. create a .env file in the root of the project
2. Add your variables like bash
3. Install dotenv library
4. In the main file, import dotenv_values from dotenv
5. Create a dotenv instance

```python
config = dotenv_values(".env")
```
6. Declare your variables using the variables created in the .env file

```python
host = config['HOST']
database = config['DATABASE']
user = config['USER']
password = config['PASSWORD']
```

