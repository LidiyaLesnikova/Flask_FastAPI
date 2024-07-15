from typing import List
from fastapi import APIRouter, Path

from db import users, database
from models.user import User, UserIn

router_user = APIRouter()

@router_user.get("/users/", response_model=List[User])
async def read_users(): 
    query = users.select()
    return await database.fetch_all(query)

@router_user.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int = Path(..., ge=1)):
    query = users.select().where(users.c.userid == user_id)
    return await database.fetch_one(query)

@router_user.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(firstname=user.firstname,
                                  lastname = user.lastname, 
                                  email=user.email,
                                  password = user.password)
    last_record = await database.execute(query)
    return {**user.dict(), "id": last_record}

@router_user.put("/users/{user_id}", response_model=User)
async def update_user(new_user: UserIn, user_id: int = Path(..., ge=1)):
    query = users.update().where(users.c.userid == user_id).values(userid=user_id, 
                                  firstname=new_user.firstname,
                                  lastname = new_user.lastname,
                                  email=new_user.email,
                                  password = new_user.password)
    record = await database.execute(query)
    return {**new_user.dict(), "id": record}

@router_user.delete("/users/{user_id}")
async def delete_user(user_id: int = Path(..., title="The ID of the user", ge=1)):
    query = users.delete().where(users.c.userid == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}