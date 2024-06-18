from fastapi import Request, HTTPException
from datetime import datetime
from fastapi.responses import RedirectResponse,JSONResponse
from app.spotifyAPI.spotify_api import use_refresh_token, get_auth_url, get_token_info
from app.CRUD.spotify import *
from app.routers.mainpage import get_deque

d = get_deque()

def login():
    #session = request.session
    #if session.get('access_token'):
    #    return RedirectResponse('/me') 
    scope = 'user-read-currently-playing user-read-recently-played user-read-private user-read-email playlist-read-private playlist-read-collaborative user-read-recently-played'
    auth_url = get_auth_url(scope)
    #auth_url = json.load(auth_url)

    return auth_url

def handle_callback(request: Request):
    user_id = d.popleft()
    if 'error' in request.query_params:
        return JSONResponse({"error": request.query_params['error']}) 
    if 'code' in request.query_params:
        token_info = get_token_info(request.query_params['code'])
        expires_at = datetime.now().timestamp() + token_info['expires_in']
        print(token_info)
        
        if insert_SpotifyInfo(user_id, token_info['access_token'], token_info['refresh_token'], expires_at):
            try:
                update_spotify_status(user_id)
                return JSONResponse(content='ok', status_code=200)
            except:
                raise HTTPException(status_code=400, detail='error')

def refresh_access_token(user_info:dict):
    
    if 'REFRESH_TOKEN' not in user_info:
        return RedirectResponse('/login')
    if datetime.now().timestamp() > user_info['EXPIRE_DATE']:
        print(user_info['REFRESH_TOKEN'])
        new_token_info = use_refresh_token(user_info['REFRESH_TOKEN'])
        print(new_token_info)
        user_info['ACCESS_TOKEN'] = new_token_info['access_token']
        user_info['EXPIRE_DATE']= datetime.now().timestamp() + new_token_info['expires_in']
        user_id = user_info['USER_ID']
        update_refreshtoken(user_id, user_info['ACCESS_TOKEN'], user_info['EXPIRE_DATE'])
        return user_info
