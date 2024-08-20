from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@
class User(BaseModel):
    username : str
    full_name : str
    email : str
    disable : bool

users_db = {
    "Brandon":{
        "username":"BrandonCF",
        "full_name":"Brandon Campos",
        "email":"Brandon@gmail.com",
        "disabled":True,
        "password":"12345678",
    },
    "Brenda":{
        "username":"BrendaSS",
        "full_name":"Brenda Saavedra ",
        "email":"BrendaSS@gmail.com",
        "disabled":True,
        "password":"12345678",
    }
    
}


# 4_10