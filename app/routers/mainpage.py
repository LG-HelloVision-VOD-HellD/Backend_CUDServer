from fastapi import APIRouter
from collections import deque
from app.spotifyAPI.spotify_user import login
router = APIRouter(prefix='/mainpage')
d = deque()


@router.post('/spotify/{user_id}') 
async def spotify_list(user_id: str):
    d.append(int(user_id))
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


def get_deque():
    return d
