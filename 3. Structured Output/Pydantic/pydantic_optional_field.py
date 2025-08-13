from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    name: str


class Course(BaseModel):
    title: str = "Introduction to Programming"
    description: Optional[str] = None # Optional field with default value None
    students: list[Student] = [{"name": "John Doe"}, {"name": "Jane Doe"}]

new_course = {}

course = Course(**new_course)
print(course)