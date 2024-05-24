from app.DB.database import engineconn
from app.DB.models import REVIEW, VOD
from sqlalchemy import *
import json
from pydantic import BaseModel
from datetime import datetime
engine = engineconn()
session_maker = engine.sessionmaker()

class Review_info(BaseModel):
    RATING : str
    COMMENT : str

def insert_reviewinfo(user_id: int, id: int, title: str, review_info : Review_info):
    try:
        
        session_maker.execute(
            insert(REVIEW),
            [
                {
                    "USER_ID" : user_id,
                    "VOD_ID" : find_vodID(id, title),
                    "RATING" : review_info.RATING,
                    "COMMENT" : review_info.COMMENT,
                    "REVIEW_WDATE" : datetime.now().strftime('%Y-%m-%d'),
                    "REVIEW_MDATE" : datetime.now().strftime('%Y-%m-%d')
                }
            ]    
        )
        session_maker.commit()
        return True
    except:
        return False
    
def find_vodID(id, title):
    try:
        VOD_ID = session_maker.execute(
            select(VOD.VOD_ID)
            .where(VOD.CONTENT_ID == id and VOD.TITLE == title)
        ).fetchall()
        print(VOD_ID[0][0])
        VOD_ID = VOD_ID[0][0]
        
        return VOD_ID   
    except:
        return 0
    
def update_reviewinfo(user_id: int, id: int, title: str, review_info : Review_info):
    VOD_ID = find_vodID(id, title)
    try:
        session_maker.execute(
           update(REVIEW)
           .where(REVIEW.VOD_ID == VOD_ID, REVIEW.USER_ID == user_id)
           .values(
                {
                    REVIEW.RATING : review_info.RATING,
                    REVIEW.COMMENT : review_info.COMMENT,
                    REVIEW.REVIEW_MDATE : datetime.now().strftime('%Y-%m-%d')
                }
            )
        )
        session_maker.commit()
        return True
    except:
        return False
     
def delete_reviewinfo(review_id: int):
     
    try:
        session_maker.execute(
            delete(REVIEW)
            .where(REVIEW.REVIEW_ID == review_id)
        )
        session_maker.commit()
        return True
    except:
        return False