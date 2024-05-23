from sqlalchemy import Column, TEXT, INT, BIGINT, DATE, VARCHAR, CHAR, SMALLINT, FLOAT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class USERS(Base):
    __tablename__ = "USERS"
    USER_ID = Column(INT, nullable=False, autoincrement = True, primary_key=True)
    SETTOP_NUM = Column(INT, nullable = False)
    USER_NAME = Column(VARCHAR(10), nullable = False)
    GENDER = Column(CHAR, nullable = True)
    AGE = Column(INT, nullable = True)
    SPOTIFY = Column(SMALLINT, nullable = True)

class ACTOR(Base):
    __tablename__ = "ACTOR"
    ACTOR_ID = Column(INT, nullable = False, autoincrement = True, primary_key = True)
    ACTOR_NAME = Column(VARCHAR, nullable = True)

class LIKES(Base):
    __tablename__ = "LIKES"
    LIKE_ID = Column(INT, nullable = False, autoincrement = True, primary_key = True)
    USER_ID = Column(INT, nullable = True)
    VOD_ID = Column(INT, nullable = True)

class REVIEW(Base):
    __tablename__ = "REVIEW"
    REVIEW_ID = Column(INT, nullable = False, autoincrement = True, primary_key = True)
    USER_ID = Column(INT, nullable = False)
    VOD_ID = Column(INT, nullable = True)
    RATING = Column(INT, nullable = False)
    COMMENT = Column(VARCHAR(150), nullable = True)
    REVIEW_WDATE = Column(DATE, nullable = True)
    REVIEW_MDATE = Column(DATE, nullable = True)
    POS_NEG = Column(SMALLINT, nullable = True)

class SPOTIFY(Base):
    __tablename__ = "SPOTIFY"
    SPOTIFY_ID = Column(INT, nullable = False, autoincrement = True, primary_key = True)
    USER_ID = Column(INT, nullable = False)
    ACCESS_TOKEN = Column(VARCHAR(255), nullable = False)
    REFRESH_TOKEN = Column(VARCHAR(255), nullable = False)
    EXPIRE_DATE = Column(FLOAT, nullable = True)
    EMOTION = Column(VARCHAR, nullable = True)
    def to_dict(self):
        return {
            "SPOTIFY_ID": self.SPOTIFY_ID,
            "USER_ID": self.USER_ID,
            "ACCESS_TOKEN": self.ACCESS_TOKEN,
            "REFRESH_TOKEN": self.REFRESH_TOKEN,
            "EXPIRE_DATE": self.EXPIRE_DATE,
            "EMOTION": self.EMOTION
        }
    
class VOD(Base):
    __tablename__ = "VOD"
    VOD_ID = Column(INT, autoincrement= True, nullable = False, primary_key= True)
    CONTENT_ID = Column(INT, nullable = False)
    SUB_CATEGORY = Column(VARCHAR(255), nullable = True)
    TITLE = Column(VARCHAR(255), nullable=False)


class MOVIES(Base):
    __tablename__ = "MOVIES"
    MOVIE_ID = Column(INT, nullable = False, primary_key = True)
    SUB_CATEGORY = Column(VARCHAR(10), nullable = False)
    TITLE = Column(VARCHAR(255), nullable = False)
    GENRE = Column(VARCHAR(10), nullable = True)
    RELEASE_DATE = Column(DATE, nullable = True)
    RATING = Column(INT, nullable = True)
    MOVIE_OVERVIEW = Column(TEXT, nullable = True)
    EMOTION = Column(VARCHAR(10), nullable = True)
    CAST = Column(VARCHAR(20), nullable = True)
    CREW = Column(TEXT, nullable = True)
    POSTER = Column(VARCHAR(255), nullable = True)
    TRAILER = Column(VARCHAR(255), nullable = True)
    LOGO = Column(VARCHAR(255), nullable = True)
    RTM = Column(INT, nullable = True)
    def to_dict(self):
        return {
            "VOD_ID": self.MOVIE_ID,
            "TITLE": self.TITLE,
            "POSTER_URL": self.POSTER
        }
    
class SERIES(Base):
    __tablename__ = "SERIES"
    SERIES_ID = Column(INT, nullable = False, primary_key = True)
    SUB_CATEGORY = Column(VARCHAR(10), nullable = True)
    TITLE = Column(VARCHAR(100), nullable = False)
    GENRE = Column(VARCHAR(10), nullable = True)
    SERIES_RATING = Column(INT, nullable = True) 
    SEASON_SUM = Column(VARCHAR(10), nullable = True)
    CAST = Column(VARCHAR(20), nullable = True)
    CREW = Column(VARCHAR(20), nullable = True)
    POSTER_URL = Column(VARCHAR(255), nullable = True)
    TRAILER_URL = Column(VARCHAR(255), nullable = True)
    RTM = Column(INT, nullable = True)
    def to_dict(self):
        return {
            "VOD_ID": self.SERIES_ID,
            "TITLE": self.TITLE,
            "POSTER_URL": self.POSTER_URL
        }
    
class SEASON(Base):
    __tablename__ = "SEASON"
    SEASON_ID = Column(INT, nullable = False, primary_key = True)
    SERIES_ID = Column(INT, nullable = False)
    SEASON_NAME = Column(VARCHAR(255), nullable = True)
    SEASON_NUM = Column(VARCHAR(10), nullable = True)
    EPISODE_COUNT = Column(INT, nullable = True)
    AIR_DATE = Column(DATE, nullable = True)

class EPISODE(Base):
    __tablename__ = "EPISODE"
    EPISODE_ID = Column(INT, nullable = False, primary_key= True)
    SEASON_ID = Column(INT, nullable = False)
    SEASON_NAME = Column(VARCHAR(255), nullable = True)
    EPISODE_NUM = Column(INT, nullable = True)
    EPISODE_NAME = Column(VARCHAR(255), nullable = True)
    EPISODE_OVERVIEW = Column(TEXT, nullable = True)
    AIR_DATE = Column(DATE, nullable = True)
    EPISODE_RTM = Column(INT, nullable = True)
    STILL = Column(VARCHAR(255), nullable = True)

