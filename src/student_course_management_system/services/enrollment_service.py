"""
Requirements:

Core logic

Comprehensions for filtering enrolled students

Polymorphic course reporting

"""


from ..models.enrollment import Enrollment


class EnrollmentService:
    def __init__(self):
        self.enrollments = []  # list of Enrollment objects

    def enroll(self, student, course):
        # Prevent duplicate enrollment
        for e in self.enrollments:
            if e.student == student and e.course == course:
                raise ValueError("Student already enrolled in this course")

        enrollment = Enrollment(student, course)
        self.enrollments.append(enrollment)
        return enrollment

    def get_student_courses(self, student):
        return [e.course for e in self.enrollments if e.student == student]

    def get_course_students(self, course):
        return [e.student for e in self.enrollments if e.course == course]
