"""
Requirements:

OOP design

Encapsulation using @property

Magic methods: __repr__, __eq__

Base class for inheritance (Graduate, Undergraduate)

"""


# models/student.py

class Student:
    """Base student entity that supports shared enrollment behavior."""

    def __init__(self, student_id, name, email):
        """Capture identity info and prepare storage for course enrollments."""
        self._student_id = student_id
        self._name = name
        self._email = email
        self._courses = []  # list of Course objects

    # ---- Properties ----
    @property
    def student_id(self):
        """Immutable ID exposed to consumers."""
        return self._student_id

    @property
    def name(self):
        """Human-readable full name."""
        return self._name
    
    @name.setter
    def name(self, new_name):
        """Allow updates when names change."""
        self._name = new_name

    @property
    def email(self):
        """Email address, kept read-only for now."""
        return self._email

    # ---- Methods ----
    def enroll(self, course):
        """Associate the student with a new course object."""
        self._courses.append(course)

    def get_courses(self):
        """Return all courses the student is attached to."""
        return self._courses

    # ---- Magic Methods ----
    def __repr__(self):
        """Debug-friendly string describing the student."""
        return f"Student({self._student_id}, {self._name})"

    def __eq__(self, other):
        """Students are equal when their IDs match."""
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False