from app.DB.database import engineconn
from app.DB.models import LIKES
from sqlalchemy import insert, delete, select, exists
from sqlalchemy.exc import OperationalError
import time
from fastapi import HTTPException

engine = engineconn()
session = engine.sessionmaker()

def insert_likeinfo(user_id: int, VOD_ID: int):
    try:
        # 존재 여부 확인
        like_exists = session.query(
            exists().where(LIKES.USER_ID == user_id).where(LIKES.VOD_ID == VOD_ID)
        ).scalar()
        
        if like_exists:
            raise HTTPException(status_code=400, detail='이미 찜 내역이 존재합니다.')  # 이미 존재하면 False 반환
        
        # 존재하지 않을 때 삽입
        session.execute(
            insert(LIKES).values(
                USER_ID=user_id,
                VOD_ID=VOD_ID
            )
        )
        session.commit()
        return True
    
    except OperationalError as e:
        if 'Lock wait timeout exceeded' in str(e):
            time.sleep(2)  # 잠시 대기 후 재시도
            return insert_likeinfo(user_id, VOD_ID)
        else:
            session.rollback()
            return False
    
    finally:
        session.close()

def delete_likeinfo(user_id: int, VOD_ID: int):
    try:
        session.execute(
            delete(LIKES)
            .where(LIKES.VOD_ID == VOD_ID, LIKES.USER_ID == user_id)
        )
        session.commit()
        return True
    except:
        session.rollback()
        return False
    finally:
        session.close()


def delete_likeinfo_user(user_id):
    try:
        session.execute(
            delete(LIKES)
            .where(LIKES.USER_ID == user_id)
        )
        session.commit()
        return True
    except:
        session.rollback()
        return False
    finally:
        session.close()
