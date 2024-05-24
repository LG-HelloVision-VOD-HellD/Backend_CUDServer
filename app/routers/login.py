from fastapi import APIRouter, HTTPException
from app.DB.models import USERS
from app.DB.database import engineconn
from sqlalchemy import select
from fastapi.responses import JSONResponse

engine = engineconn()
session_maker = engine.sessionmaker()
router = APIRouter(prefix='/users')


@router.get('/{settop_id}')
def login(settop_id: str):
    settop_user_list = session_maker.execute(
        select(USERS.USER_NAME, USERS.USER_ID)
        .where(USERS.SETTOP_NUM == settop_id)
    ).fetchall()

    user_list = [
        {'user_name': user[0], 'user_id': user[1]}
        for user in settop_user_list
    ]

    if user_list:
        return JSONResponse({'user_list': user_list})
    else:
        raise HTTPException(status_code=400, detail="Users not found")
