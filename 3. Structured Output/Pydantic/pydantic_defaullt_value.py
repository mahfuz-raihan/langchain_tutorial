from pydantic import BaseModel

class Student(BaseModel):
    name: str


class Course(BaseModel):
    title: str = "Introduction to Programming"
    description: str = "A course on programming fundamentals."
    students: list[Student] = [{"name": "John Doe"}, {"name": "Jane Doe"}]

new_course = {}

course = Course(**new_course)
print(course)