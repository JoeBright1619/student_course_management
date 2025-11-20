"""
Requirements:

Functions

Lists/dictionaries/sets

Comprehensions

Modular code

/ *args / **kwargs

"""


from ..models.student import Student
from ..models.undergraduate import Undergraduate
from ..models.graduate import Graduate


class StudentService:
    def __init__(self):
        self.students = {}  # key: student_id, value: Student object

    def add_student(self, student_type, *args, **kwargs):
        student = student_type(*args, **kwargs)

        if student.student_id in self.students:
            raise ValueError("Student already exists")

        self.students[student.student_id] = student
        return student

    def get_student(self, student_id):
        return self.students.get(student_id)

    def list_students(self):
        return list(self.students.values())

    def filter_by_major(self, major):
        return [s for s in self.students.values() if s.major == major]
