from fastapi import FastAPI,Depends
# from pydantic import BaseModel
from schema import Student,StudentBase,StudentCreate,StudentPublic,StudentUpdate
from database import get_db, SessionLocal,engine
from sqlmodel import SQLModel
from contextlib import asynccontextmanager
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException


@asynccontextmanager
async def lifespan(app:FastAPI):
    SQLModel.metadata.create_all(engine)
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/students", response_model=StudentPublic)
def create_student(student: Student ,db: Session =Depends(get_db)):
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@app.get("/students")
def get_students(db:Session=Depends(get_db)): 
    students=db.execute(select(Student)).scalars().all()
    print(students)
    
    return students

@app.get("/students/{student_id}")
def get_student(student_id:int ,db:Session=Depends(get_db)):
    student=db.get(Student,student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.patch("/students/{student_id}")
def update_student_name(student_id:int, db:Session=Depends(get_db)):
    student =db.get(Student,student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    else:
        student.name="abc"
        db.commit()
        db.refresh(student)
    return student