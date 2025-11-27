"""
Requirements:

OOP

Magic methods (__repr__)

Supports polymorphic reporting

"""

# models/course.py

class Course:
    """Domain object that tracks a course roster and simple analytics."""

    def __init__(self, course_code, title, max_students=30):
        """Store identifying data and prepare an empty student roster."""
        self.course_code = course_code
        self.title = title
        self.max_students = max_students
        self._students = []  # list of Student objects

    def add_student(self, student):
        """Append a student if capacity allows, otherwise warn the caller."""
        if len(self._students) < self.max_students:
            self._students.append(student)
        else:
            print("Course is full!")

    def get_students(self):
        """Return the raw list so callers can inspect enrollment."""
        return self._students

    def calculate_average(self, *grades):
        """Compute the arithmetic mean of any grades supplied."""
        if grades:
            return sum(grades) / len(grades)
        return 0

    def __repr__(self):
        """Helpful representation for debugging/menus."""
        return f"Course({self.course_code}, {self.title})"

    def __eq__(self, other):
        """Courses are equal when they share the same code."""
        if isinstance(other, Course):
            return self.course_code == other.course_code
        return False