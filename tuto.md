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

