from fastapi import APIRouter, HTTPException
from app.DB.models import USERS
from app.DB.database import engineconn
from sqlalchemy import select
from app.CRUD.spotify import check_Spotify_accesstoken, vodlist_match_useremotion, select_SpotifyInfo, update_emotion, update_spotify_status
from app.spotify_api import get_playlist
from collections import deque
from datetime import datetime

router = APIRouter(prefix='/mainpage')
d = deque()

@router.get('/')
async def example():
    return {'message': 'hello'}

@router.get('/spotify/{user_id}') 
async def spotify_list(user_id: str):
    if check_Spotify_accesstoken(user_id):
        data = vodlist_match_useremotion(user_id)
    else:
        d.append(int(user_id))
        from spotify_user import login  # 필요한 경우에만 임포트
        url = login()
        data = {'status': False, 'response': url}
    
    return data

'''@router.get('/spotify/{user_id}/userinfo')
async def get_emotion(user_id: str):
    try:
        user_info = select_SpotifyInfo(user_id)
        if not user_info or datetime.now().timestamp() > user_info[0]['EXPIRE_DATE']:
            from spotify_user import refresh_access_token  # 필요한 경우에만 임포트
            user_info = refresh_access_token(user_info[0]) if user_info else login()
        
        audio_names = get_playlist(user_info['ACCESS_TOKEN'])
        lyrics_list = crawling_lyrics(audio_names)
        emotion = predict_emotion(lyrics_list)
        
        update_emotion(user_id, emotion)
        data = vodlist_match_useremotion(user_id)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))'''

@router.get('/youtube')
async def youtube_list():
    raise HTTPException(status_code=501, detail="Not Implemented")

@router.get('/popular_vod')
async def popular_vod_list():
    raise HTTPException(status_code=501, detail="Not Implemented")

def get_deque():
    return d
