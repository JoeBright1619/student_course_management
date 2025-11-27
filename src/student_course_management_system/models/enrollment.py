"""
Requirements:

Flexible data structures

Magic methods (__repr__)

"""

# models/enrollment.py

class Enrollment:
    """Tie together a student, a course, and their optional score."""

    def __init__(self, student, course, score=None):
        """Store links to the student/course pair plus any grade."""
        self.student = student
        self.course = course
        self.score = score

    def __repr__(self):
        """Readable mapping of which student is in which course."""
        return f"Enrollment(Student={self.student.name}, Course={self.course.title})"

    def __eq__(self, other):
        """Uniqueness is based on the student-course combination."""
        if isinstance(other, Enrollment):
            return self.student == other.student and self.course == other.course
        return False