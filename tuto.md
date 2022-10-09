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

SQLAlchemy
We need a driver for the database we want to use. In this case we are using postgres with psycopg2.
The file database.py handles the database connection
The file models will represent our tables

Creating User Account
First thing we need is to define our model (create a table in postgres database to hold all user info),
Because we're using SQLAlchemy we need to create an ORM model, to define what our postgres table looks like.
So first thing, go to the models file and create a model for the user table

Then we create a UserCreate schema

We also need to create the users endpoint in our main file

Now, we need to hash the password for user
```
    pip install "passlib[bcrypt]"
```
In the create user endpoint function, before creating the user, create the hash
```python
hashed_password = pwd_context.hash(user.password)
```
Then update the pydant model:
```python
user.password = hashed_password
```

Abstract the hashing logic to its own function in a file called utils.py

Next step is to refactor our main file, and separate the calls for posts and users
Create a folder called routes and inside it, two files: post.py and user.py
Now move the corresponding code to its file, and all the needed imports
We will need to set up routes for all calls, as we are not in our main app anymore
import APIRouter from fastapi, create an instance and save it in a routes variable
replace @app.get... to @router...
In the main file import post and user from routers