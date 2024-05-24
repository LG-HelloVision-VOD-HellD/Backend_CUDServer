from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from app.DB.database import engineconn
from sqlalchemy import *
from fastapi.responses import JSONResponse
from app.CRUD.user_info import insert_userinfo, update_userinfo, delete_userinfo
engine = engineconn()
session_maker = engine.sessionmaker()
router = APIRouter(prefix='/user')
class User_info(BaseModel):
     SETTOP_NUM : str
     USER_NAME : str
     GENDER : str
     AGE : int



@router.post('/')
def insert_user(signup: User_info):
    result = insert_userinfo(signup)
    if result:
        return JSONResponse(content={'response': 'FINISH INSERT USERS'}, status_code= 200)
    else :
        return JSONResponse(content={'error' : 'EMPTY_SIGNUP_ELEMENTS'}, status_code = 400)
    

@router.put('/{user_id}')
def update_user(user_info: User_info, user_id: int):
    result = update_userinfo(user_id, user_info)
    if result:
        return JSONResponse(content={'response': 'FINISH UPDATE USERS'}, status_code= 200)
    else :
        return JSONResponse(content={'error' : 'EMPTY_SIGNUP_ELEMENTS'}, status_code = 400)
    

@router.get('/{user_id}')
def read_userinfo(user_id: int):
    #mongoDB
    return 0

@router.delete('/{user_id}')
def delete_user(user_id: int):
    result = delete_userinfo(user_id)
    if result:
        return JSONResponse(content={'response': 'FINISH DELETE USERS'}, status_code= 200)
    else :
        return JSONResponse(content={'error' : 'EMPTY_SIGNUP_ELEMENTS'}, status_code = 400)
    