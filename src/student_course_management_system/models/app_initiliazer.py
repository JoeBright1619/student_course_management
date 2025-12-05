from src.student_course_management_system.models.undergraduate import Undergraduate
from src.student_course_management_system.models.graduate import Graduate
from src.student_course_management_system.services.student_service import StudentService
from src.student_course_management_system.services.course_service import CourseService
from src.student_course_management_system.services.enrollment_service import EnrollmentService
from src.student_course_management_system.services.report_service import SummaryReport

class AppInitializer:
    @staticmethod
    def bootstrap():
        """Initialize the system with sample students, courses, and enrollments."""

       # Initialize services
        student_service = StudentService()
        course_service = CourseService()
        enrollment_service = EnrollmentService()
        report_service = SummaryReport()

        # --- Create sample students ---
        s1 = student_service.add_student(
            Undergraduate,
            student_id=101,
            name="Bright",
            email="bright@example.com",
            level="Year 2"
        )

        s2 = student_service.add_student(
            Undergraduate,
            student_id=102,
            name="Alice",
            email="alice@example.com",
            level="Year 1"
        )

        s3 = student_service.add_student(
            Graduate,
            student_id=201,
            name="David",
            email="david@example.com",
            thesis_topic="Machine Learning Optimization"
        )

        # --- Create sample courses ---
        c1 = course_service.add_course("CS101", "Intro to Computer Science", max_students=50)
        c2 = course_service.add_course("CS201", "Data Structures", max_students=40)
        c3 = course_service.add_course("CS301", "Advanced AI", max_students=25)

        # --- Enroll students ---
        enrollment_service.enroll_student(s1, c1)
        enrollment_service.enroll_student(s1, c2)
        enrollment_service.enroll_student(s2, c1)
        enrollment_service.enroll_student(s2, c2)
        enrollment_service.enroll_student(s3, c3)
        
        enrollment_service.assign_grade(s1, c1, 98)
        enrollment_service.assign_grade(s2, c1, 60)
        enrollment_service.assign_grade(s1, c2, 100)
        enrollment_service.assign_grade(s2, c2, 70)
        enrollment_service.assign_grade(s3, c3, 57)
        # --- Return all services so the app can use them anywhere ---
        return {
            "students": student_service,
            "courses": course_service,
            "enrollments": enrollment_service,
            "reports": report_service
        }
