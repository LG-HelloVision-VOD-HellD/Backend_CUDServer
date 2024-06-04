from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.sessions import SessionMiddleware
from app.spotifyAPI.spotify_user import handle_callback
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from app.DB.database import engineconn
from app.CRUD.spotify import *
from app.routers.user_info import router as userinfo_router
from app.routers.mainpage import router as mainpage_router
from app.routers.search import router as search_router
from app.routers.like import router as like_router
from app.routers.review import router as review_router
import uvicorn


app = FastAPI()



app.add_middleware(SessionMiddleware, secret_key="your_secret_key")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # 허용할 origin을 설정하세요
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(userinfo_router)
app.include_router(mainpage_router)
app.include_router(search_router)
app.include_router(review_router)
app.include_router(like_router)



@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={'error': 'UNPROCESSABLE_ENTITY', 'details': 'error'},
    )

emotion_test = ''
@app.get('/')
async def index():
    return {"message": "Hello World"}

@app.get('/callback')
async def callback(request: Request):
    return handle_callback(request)



'''@app.get('/refresh-token')
def refresh_token(request: Request):
    return refresh_access_token(request)
'''
if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=80, reload=True)