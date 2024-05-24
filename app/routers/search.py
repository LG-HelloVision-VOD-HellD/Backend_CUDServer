from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from app.DB.models import VOD
from app.DB.database import engineconn
from sqlalchemy import *
engine = engineconn()
session_maker = engine.sessionmaker()
router = APIRouter(prefix='/search')

@router.get('/{keyword}')
async def search(keyword: str):
    if keyword:
        vod_title_list = session_maker.execute(
            select(VOD.TITLE, VOD.VOD_ID).
            where((VOD.GENRE.like(f'%{keyword}%')) | (VOD.CAST.like(f'%{keyword}%')) | (VOD.TITLE.like(f'%{keyword}%')))
        )
        vod_list = []
        for vod in list(vod_title_list):
                print(vod[0])
                print(vod[1])
                vod_list.append(
                    {
                     'vod_title':vod[0],
                     'vod_id':vod[1]
                    }
                )
        if vod_list:
            #print(len(sq_user_list))
            print(vod_list)
            vods = {
                'vod_list' : vod_list
            }
            return JSONResponse(vods)
        else:
            print("error")
            return JSONResponse(content='error', status_code=402)
    else:
        result = {
            'check_response': 'error'
        }
        return JSONResponse(result)