from DB.database import engineconn
from DB.models import LIKES, VOD
from sqlalchemy import *

engine = engineconn()
session_maker = engine.sessionmaker()

def find_vodID(id, title):
    try:
        VOD_ID = session_maker.execute(
            select(VOD.VOD_ID)
            .where(VOD.CONTENT_ID == id and VOD.TITLE == title)
        )
        return VOD_ID   
    except:
        return 0

def insert_likeinfo(user_id: int, id: int, title: str):
    try:
        session_maker.execute(
            insert(LIKES),
            [
                {
                    "USER_ID" : user_id,
                    "VOD_ID" : find_vodID(id, title),
                }
            ]    
        )
        session_maker.commit()
        return True
    except:
        return False
    

def delete_likeinfo(user_id: int, id: int, title: str):
    
    try:
        VOD_ID = find_vodID(id, title)
        session_maker.execute(
            delete(LIKES)
            .where(LIKES.VOD_ID == VOD_ID, LIKES.USER_ID == user_id)
        )
        session_maker.commit()
        return True
    except:
        return False