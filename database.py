from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


URL="postgresql://postgress:123456@localhost:5432/student"

db=create_engine(URL)

SessionLocal=sessionmaker(
    bind=db,
    autoflush=False,
    autocommit=False
)

class Base(DeclarativeBase):
    pass

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()