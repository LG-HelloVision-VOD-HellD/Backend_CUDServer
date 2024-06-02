from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.CRUD.like import *

router = APIRouter(prefix='/like')
@router.post('/{user_id}')
def insert_review(user_id: int, id: int, title: str):
    result = insert_likeinfo(user_id, id, title)
    if result:
        return JSONResponse(content={'response': 'FINISH INSERT REVIEW'}, status_code= 200)
    else:
        return JSONResponse(content={'response': 'ERROR INSERT REVIEW'}, status_code= 400)

@router.delete('/{user_id}')
def update_review(user_id: int, id: int, title: str):
    result = delete_likeinfo(user_id, id, title)
    if result:
        return JSONResponse(content={'response': 'FINISH UPDATE REVIEW'}, status_code= 200)
    else:
        return JSONResponse(content={'response': 'ERROR INSERT REVIEW'}, status_code= 400)

