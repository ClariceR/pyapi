from datetime import date, datetime
from xmlrpc.client import _datetime
from jose import JWTError, jwt
from datetime import datetime, timedelta

from dotenv import dotenv_values

config = dotenv_values(".env")

SECRET_KEY = config['SECRET_KEY']
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

