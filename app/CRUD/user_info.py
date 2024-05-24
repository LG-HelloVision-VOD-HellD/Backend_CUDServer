from app.DB.database import engineconn
from app.DB.models import USERS
from sqlalchemy import *
import json
from pydantic import BaseModel
engine = engineconn()
session_maker = engine.sessionmaker()

class User_info(BaseModel):
     SETTOP_NUM : str
     USER_NAME : str
     GENDER : str
     AGE : int

def insert_userinfo(user_info : User_info):
     
     if user_info:
          SETTOP_NUM = user_info.SETTOP_NUM.replace('"', '')
          session_maker.execute(
               insert(USERS),
               [
                    {
                    "SETTOP_NUM" : SETTOP_NUM,
                    "USER_NAME" : user_info.USER_NAME,
                    "GENDER" : user_info.GENDER,
                    "AGE" : int(user_info.AGE),
                    }
               ]
          )
          session_maker.commit()
          return True
     else:
          return False

def update_userinfo(user_id, user_info : User_info):
     
     if User_info:
          session_maker.execute(
               update(USERS)
               .where(USERS.USER_ID == user_id)
               .values(
                    {
                         USERS.USER_NAME : user_info.USER_NAME,
                         USERS.AGE : user_info.AGE,
                         USERS.GENDER : user_info.GENDER
                    }
               )
          )
          session_maker.commit()
          return True
     else:
          return False
     
def delete_userinfo(user_id):
     
     if user_id:
          session_maker.execute(
               delete(USERS)
               .where(USERS.USER_ID == user_id)
          )
          session_maker.commit()
          return True
     else:
          return False