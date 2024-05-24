from fastapi import APIRouter
from app.DB.database import engineconn
from fastapi.responses import JSONResponse
from app.CRUD.like import *

engine = engineconn()
session_maker = engine.sessionmaker()
router = APIRouter(prefix='/like')

@router.post('/user_id={user_id}/vod_id={id}/title={title}')
def insert_review(user_id: int, id: int, title: str):
    result = insert_likeinfo(user_id, id, title)
    if result:
        return JSONResponse(content={'response': 'FINISH INSERT REVIEW'}, status_code= 200)
    else:
        return JSONResponse(content={'response': 'ERROR INSERT REVIEW'}, status_code= 400)

@router.delete('/user_id={user_id}/vod_id={id}/title={title}')
def update_review(user_id: int, id: int, title: str):
    result = delete_likeinfo(user_id, id, title)
    if result:
        return JSONResponse(content={'response': 'FINISH UPDATE REVIEW'}, status_code= 200)
    else:
        return JSONResponse(content={'response': 'ERROR INSERT REVIEW'}, status_code= 400)

