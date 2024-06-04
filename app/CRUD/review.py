from app.DB.database import engineconn
from app.DB.models import REVIEW, VOD
from sqlalchemy import *
from pydantic import BaseModel
from datetime import datetime
engine = engineconn()
session_maker = engine.sessionmaker()

class Review_info(BaseModel):
    VOD_ID : int
    RATING : str
    COMMENT : str

def insert_reviewinfo(user_id: int, review_info : Review_info):
    try:
        session_maker.execute(
            insert(REVIEW),
            [
                {
                    "USER_ID" : user_id,
                    "VOD_ID" : review_info.VOD_ID,
                    "RATING" : review_info.RATING,
                    "COMMENT" : review_info.COMMENT,
                    "W_DATE" : datetime.now().strftime('%Y-%m-%d'),
                    "M_DATE" : datetime.now().strftime('%Y-%m-%d')
                }
            ]    
        )
        session_maker.commit()
        return True
    except:
        session_maker.rollback()
        return False
    finally:
        session_maker.close()
    
def update_reviewinfo(user_id: int, review_info : Review_info):
    try:
        session_maker.execute(
           update(REVIEW)
           .where(REVIEW.VOD_ID == review_info.VOD_ID, REVIEW.USER_ID == user_id)
           .values(
                {
                    REVIEW.RATING : review_info.RATING,
                    REVIEW.COMMENT : review_info.COMMENT,
                    REVIEW.M_DATE : datetime.now().strftime('%Y-%m-%d')
                }
            )
        )
        session_maker.commit()
        return True
    except:
        session_maker.rollback()
        return False
    finally:
        session_maker.close()
     
def delete_reviewinfo(review_id: int):
     
    try:
        session_maker.execute(
            delete(REVIEW)
            .where(REVIEW.REVIEW_ID == review_id)
        )
        session_maker.commit()
        return True
    except:
        session_maker.rollback()
        return False
    finally:
        session_maker.close()

def delete_reviewinfo_user(user_id: int):
     
    try:
        session_maker.execute(
            delete(REVIEW)
            .where(REVIEW.USER_ID == user_id)
        )
        session_maker.commit()
        return True
    except:
        session_maker.rollback()
        return False
    finally:
        session_maker.close()