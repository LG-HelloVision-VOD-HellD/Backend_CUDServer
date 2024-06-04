import urllib.parse
import requests
from datetime import datetime, timedelta
import os
import base64
from dotenv import load_dotenv
load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

REDIRECT_URI = 'http://hellodycud-264244293.ap-northeast-2.elb.amazonaws.com/callback'
#REDIRECT_URI = 'http://localhost:8000/callback'
AUTH_URL = 'https://accounts.spotify.com/authorize'
TOKEN_URL = 'https://accounts.spotify.com/api/token'
API_BASE_URL = 'https://api.spotify.com/v1/'
'''def generate_code_verifier(length=43):
    # 랜덤 바이트를 생성하여 base64로 인코딩합니다.
    code_verifier = base64.urlsafe_b64encode(os.urandom(length)).decode().rstrip('=')
    return code_verifier

# 사용 예시
CODE_VERIFIER = generate_code_verifier()
CODE_CHALLENGE = pkce.get_code_challenge(CODE_VERIFIER)'''

def get_auth_url(scope):
    params = {
        'client_id' : CLIENT_ID,
        'response_type' : 'code',
        'scope' : scope,
        'redirect_uri' : REDIRECT_URI
    } 

    return f"{AUTH_URL}?{urllib.parse.urlencode(params)}"
    
def get_token_info(code):
    req_body = {
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(TOKEN_URL, data=req_body)
    token_info = response.json()

    return token_info

def use_refresh_token(refresh_token):
    req_body = {
        'grant_type' : 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(TOKEN_URL, data=req_body)
    return response.json()
