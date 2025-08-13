from pydantic import BaseModel, EmailStr , Field
from typing import Optional



class Student(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int]
    cgpa: float = Field(gt=0, lt=10, default=5) # example with field


class Course(BaseModel):
    title: str = "Introduction to Programming"
    description: Optional[str] = None # Optional field with default value None
    # students: list[Student] = [{"name": "John Doe","email":"abc@gmail.com"}, {"name": "Jane Doe", "email":"trd"}]

# new_course = {}
new_student = {"name": "John Doe","email":"abcg@mail.com", "age":21, "cgpa":5}
# course = Course(**new_course)
student = Student(**new_student)
print(student)