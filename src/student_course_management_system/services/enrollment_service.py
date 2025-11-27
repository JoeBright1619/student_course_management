"""
Requirements:

Core logic

Comprehensions for filtering enrolled students

Polymorphic course reporting

"""


from ..models.enrollment import Enrollment


class EnrollmentService:
    """Coordinates relationships between students, courses, and grades."""

    def __init__(self):
        self.enrollments = []  # list of Enrollment objects

    def enroll_student(self, student, course):
        """Create an enrollment record while preventing duplicates."""
        enrollment = Enrollment(student, course)

        if enrollment in self.enrollments:  # prevent duplicate enrollment
            raise ValueError("Student already enrolled in this course")

        self.enrollments.append(enrollment)
        return enrollment
    
    def assign_grade(self, student, course, score):
        """Attach a numeric grade to an existing enrollment."""
        for e in self.enrollments:
            if e.student == student and e.course == course:
                e.score = score
                return e
        raise ValueError("Enrollment not found")
    
    def get_course_average(self, course):
        """Return average of all recorded grades for the course."""
        grades = [e.score for e in self.enrollments if e.course == course and e.score is not None]
        return sum(grades) / len(grades) if grades else None


    def get_student_courses(self, student):
        """List all courses a particular student is tied to."""
        return [e.course for e in self.enrollments if e.student == student]

    def get_course_students(self, course):
        """List all students currently linked to a course."""
        return [e.student for e in self.enrollments if e.course == course]
