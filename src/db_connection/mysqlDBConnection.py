import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

load_dotenv()

class DBConnection:
    _engine = None

    def __init__(self):
        if DBConnection._engine is None:
            self.user = os.getenv('DB_USER')
            self.password = os.getenv('DB_PASSWORD')
            self.host = os.getenv('DB_HOST')
            self.port = os.getenv('DB_PORT')
            self.database = os.getenv('DB_NAME')

            DBConnection._engine = create_engine(
                f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}',
                echo=False,
                poolclass=QueuePool,
                pool_size=5,
                max_overflow=5,
                pool_recycle=1800,
                pool_timeout = 30
            )

    def create_db_connection(self):
        return DBConnection._engine
