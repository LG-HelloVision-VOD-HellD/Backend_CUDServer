from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from DB.models import USERS
from DB.database import engineconn
from sqlalchemy import *
from fastapi.responses import JSONResponse
engine = engineconn()
session_maker = engine.sessionmaker()
router = APIRouter(prefix='/login')
class Settop_id(BaseModel):
    settop_num : str
@router.post('/')
async def login(settop_id : Settop_id):
    if settop_id:
        settop_user_list = session_maker.execute(
            select(USERS.USER_NAME, USERS.USER_ID).
            where(USERS.SETTOP_NUM == settop_id.settop_num))
        user_list = []
        for user in list(settop_user_list):
                print(user[0])
                print(user[1])
                user_list.append(
                    {
                     'user_name':user[0],
                     'user_id':user[1]
                    }
                )
        if user_list:
            #print(len(sq_user_list))
            print(user_list)
            user = {
                'user_list' : user_list
            }
            return JSONResponse(user)
        else:
            print("error")
            return JSONResponse(content='error', status_code=402)
    else:
        result = {
            'check_response': 'error'
        }
        return JSONResponse(result)