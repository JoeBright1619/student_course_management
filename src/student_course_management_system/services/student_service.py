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
    """Lightweight repository for managing student objects."""

    def __init__(self):
        self.students = []  # Array of Objects

    def add_student(self, student_type, *args, **kwargs):
        """Instantiate the supplied class and keep the instance if unique."""
        student = student_type(*args, **kwargs)

        if student in self.students:
            raise ValueError("Student already exists")

        self.students.append(student)
        return student

    def get_student(self, student_id):
        """Linear search for a student by ID."""
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def list_students(self):
        """Expose the internal list to callers for iteration/display."""
        return self.students

    def filter_by_major(self, major):
        """Example filter demonstrating list comprehension usage."""
        return [s for s in self.students.values() if s.major == major]
