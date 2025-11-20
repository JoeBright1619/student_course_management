"""
Requirements:

Flexible data structures

Magic methods (__repr__)

"""

# models/enrollment.py

class Enrollment:
    def __init__(self, student, course, score=None):
        self.student = student
        self.course = course
        self.score = score

    def __repr__(self):
        return f"Enrollment(Student={self.student.name}, Course={self.course.title})"

    def __eq__(self, other):
        if isinstance(other, Enrollment):
            return self.student == other.student and self.course == other.course
        return False