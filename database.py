from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


URL="postgresql://postgres:123456@localhost:5432/student"

engine=create_engine(URL)

SessionLocal=sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()