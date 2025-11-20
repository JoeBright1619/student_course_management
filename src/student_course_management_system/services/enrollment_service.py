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

    def enroll_student(self, student, course):
        enrollment = Enrollment(student, course)

        if enrollment in self.enrollments:  # prevent duplicate enrollment
            raise ValueError("Student already enrolled in this course")

        self.enrollments.append(enrollment)
        return enrollment

    def get_student_courses(self, student):
        return [e.course for e in self.enrollments if e.student == student]

    def get_course_students(self, course):
        return [e.student for e in self.enrollments if e.course == course]
