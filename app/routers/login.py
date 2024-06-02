from fastapi import APIRouter, HTTPException
from DB.models import USERS
from DB.database import engineconn
from sqlalchemy import select
from fastapi.responses import JSONResponse

engine = engineconn()
session_maker = engine.sessionmaker()
router = APIRouter(prefix='/users')

