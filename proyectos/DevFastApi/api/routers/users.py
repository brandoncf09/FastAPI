from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Iniciar el servidor con el comando uvicorn api.users:app --reload

# Entidad user


class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int


users_list = [User(id=1, name="Brandon", surname="BrandonCF", url="www.google.com", age=35),
              User(id=2, name="Juan", surname="JuanCF",
                   url="www.google.com", age=20),
              User(id=3, name="Carlos", surname="CarlosCF", url="www.google.com", age=25)]


@router.get("/usersjson")
async def usersjson():
    return [{"name": "Brandon", "surname": "BrandonCF", "url": "www.google.com", "age": 35},
            {"name": "Juan", "surname": "JuanCF",
                "url": "www.google.com", "age": 20},
            {"name": "Carlos", "surname": "CarlosCF", "url": "www.google.com", "age": 25}]


@router.get("/users")
async def users():
    return users_list

# path


@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

# Query
@router.get("/user/")
async def user(id: int):
    return search_user(id)

# Insertar datos
@router.post("/user/", status_code=201)
async def user(user:User):
    if type(search_user(user.id)) == User:
        
        raise HTTPException(status_code=404, detail="El usuario ya existe")
        
    
    users_list.append(user)
    return user
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
@router.put("/user/")
async def user(user:User):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    
        if not found:
            return {"error":"No se ha actualizado al usuario"}
        
        return user

@router.delete("/user/{id}")
async def user(id:int):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"error":" No se ha eliminado el usuario"}


def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}


