from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()
USERNAME = os.getenv("DATABASE_USERNAME")
PASSWORD = os.getenv("DATABASE_PASSWORD")
HOST = os.getenv("DATABASE_HOSTAME")
PORT = os.getenv("DATABASE_PORT")
DB = os.getenv("DATABASE_NAME")
DB_URL = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB}'

class engineconn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle = 500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connection(self):
        conn = self.engine.connect()
        return conn