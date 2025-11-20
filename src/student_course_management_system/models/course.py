"""
Requirements:

OOP

Magic methods (__repr__)

Supports polymorphic reporting

"""

# models/course.py

class Course:
    def __init__(self, course_code, title, max_students=30):
        self.course_code = course_code
        self.title = title
        self.max_students = max_students
        self._students = []  # list of Student objects

    def add_student(self, student):
        if len(self._students) < self.max_students:
            self._students.append(student)
        else:
            print("Course is full!")

    def get_students(self):
        return self._students

    def calculate_average(self, *grades):
        if grades:
            return sum(grades) / len(grades)
        return 0

    def __repr__(self):
        return f"Course({self.course_code}, {self.title})"
