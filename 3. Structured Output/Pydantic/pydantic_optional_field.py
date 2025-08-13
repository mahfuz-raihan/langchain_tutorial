from pydantic import BaseModel, EmailStr 
from typing import Optional
import email_validator


class Student(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int]


class Course(BaseModel):
    title: str = "Introduction to Programming"
    description: Optional[str] = None # Optional field with default value None
    students: list[Student] = [{"name": "John Doe","email":"abc@gmail.com", "age":34}, {"name": "Jane Doe", "email":"trd"}]

new_course = {}

course = Course(**new_course)
print(course)