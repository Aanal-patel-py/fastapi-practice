from pydantic import BaseModel,Field
from sqlmodel import Field,SQLModel

class StudentBase(SQLModel):
    name: str =Field(max_length=20)
    rollno: int=Field(gt=0)
    standard: int=Field(gt=0,lt=13)


class Student(StudentBase,table=True):
    id:int|None = Field(default=None, primary_key=True)
    password: str

class StudentPublic(StudentBase):
    id:int

class StudentCreate(StudentBase):
    password:str

class StudentUpdate(StudentBase):
    name: str|None=None
    rollno: int|None=None
    standard:int|None=None
    password: str|None=None
