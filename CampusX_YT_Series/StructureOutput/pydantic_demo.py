from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):

    name: str = "nitish"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10)


new_student = {"age": "32", "email": "aakash.jha@gmail.com", "cgpa": 9}

student = Student(**new_student)
print(student)

student_dict = dict(student)

print(student_dict["age"])

student_json = student.model_dump_json()

print(student_json)
