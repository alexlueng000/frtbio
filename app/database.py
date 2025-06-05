# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError

DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/bidding_emails?charset=utf8mb4"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 用于依赖注入
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

