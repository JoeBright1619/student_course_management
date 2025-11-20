"""
Requirements:

OOP design

Encapsulation using @property

Magic methods: __repr__, __eq__

Base class for inheritance (Graduate, Undergraduate)

"""


# models/student.py

class Student:
    def __init__(self, student_id, name, email):
        self._student_id = student_id
        self._name = name
        self._email = email
        self._courses = []  # list of Course objects

    # ---- Properties ----
    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def email(self):
        return self._email

    # ---- Methods ----
    def enroll(self, course):
        self._courses.append(course)

    def get_courses(self):
        return self._courses

    # ---- Magic Methods ----
    def __repr__(self):
        return f"Student({self._student_id}, {self._name})"
