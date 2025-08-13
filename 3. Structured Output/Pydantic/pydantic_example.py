from pydantic import BaseModel

class Student(BaseModel):
    name: str


class Course(BaseModel):
    title: str
    description: str
    students: list[Student]

new_course = {
    "title": "Introduction to Python",
    "description": "A beginner's course on Python programming.",
    "students": [
        {"name": "Alice"},
        {"name": "Bob"}
    ]
}

course = Course(**new_course)
print(course)