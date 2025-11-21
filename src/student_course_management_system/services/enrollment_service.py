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
    
    def assign_grade(self, student, course, score):
        for e in self.enrollments:
            if e.student == student and e.course == course:
                e.score = score
                return e
        raise ValueError("Enrollment not found")
    
    def get_course_average(self, course):
        grades = [e.score for e in self.enrollments if e.course == course and e.score is not None]
        return sum(grades) / len(grades) if grades else None


    def get_student_courses(self, student):
        return [e.course for e in self.enrollments if e.student == student]

    def get_course_students(self, course):
        return [e.student for e in self.enrollments if e.course == course]
