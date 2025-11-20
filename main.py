"""Requirements covered:

Control flow

Menu-driven logic

Connecting all modules

No heavy logic here — just orchestrates everything."""

# main.py
from src.student_course_management_system.models.undergraduate import Undergraduate
from src.student_course_management_system.models.graduate import Graduate
from src.student_course_management_system.services.student_service import StudentService
from src.student_course_management_system.services.course_service import CourseService
from src.student_course_management_system.services.enrollment_service import EnrollmentService
from src.student_course_management_system.services.report_service import SummaryReport
from src.student_course_management_system.utils.menu import main_menu, pause, student_type_menu
from src.student_course_management_system.utils.input_handlers import is_valid_email, is_non_empty_string, is_valid_int


# Initialize services
student_service = StudentService()
course_service = CourseService()
enrollment_service = EnrollmentService()
report_service = SummaryReport()


# Main loop
while True:
    choice = main_menu()

    if choice == "1":  # Add Student
        stype = student_type_menu()
        name = input("Enter student name: ")
        email = input("Enter student email: ")

        if not is_non_empty_string(name):
            print("Name cannot be empty.")
            pause()
            continue
        if not is_valid_email(email):
            print("Invalid email.")
            pause()
            continue

        student_id = len(student_service.students) + 1  # simple ID generator

        if stype == "1":
            level = input("Enter undergraduate year (1-4): ")
            if not is_valid_int(level):
                print("Invalid year.")
                pause()
                continue
            student_service.add_student(
                Undergraduate,  # pass the class itself
                student_id,
                name,
                email,
                int(level)  # constructor args
            )
        elif stype == "2":  # Graduate
            thesis = input("Enter thesis topic: ")
            student_service.add_student(
                Graduate,  # class
                student_id,
                name,
                email,
                thesis
            )

        else:
            print("Invalid student type.")
            pause()
            continue

        
        print(f"Added {name} successfully!")
        pause()

    elif choice == "2":  # Add Course
        course_code = input("Enter course code: ")
        title = input("Enter course title: ")
        if not is_non_empty_string(course_code) or not is_non_empty_string(title):
            print("Course code/title cannot be empty.")
            pause()
            continue
        course_service.add_course(course_code, title)
        print(f"Course {title} added successfully!")
        pause()

    elif choice == "3":  # Enroll Student
        student_id = input("Enter student ID to enroll: ")
        course_code = input("Enter course code: ")

        if not is_valid_int(student_id):
            print("Invalid student ID.")
            pause()
            continue

        student = student_service.get_student(int(student_id))
        course = course_service.get_course(course_code)

        if not student or not course:
            print("Student or course not found.")
            pause()
            continue

        enrollment_service.enroll(student, course)
        print(f"{student.name} enrolled in {course.title} successfully!")
        pause()

    elif choice == "4":  # View Students
        students = student_service.list_students()
        print("\nStudents List:")
        for s in students:
            print(f"{s.student_id} | {s.name} | {s.email}")
        pause()

    elif choice == "5":  # View Courses
        courses = course_service.list_courses()
        print("\nCourses List:")
        for c in courses:
            print(f"{c.course_code} | {c.title}")
        pause()

    elif choice == "6":  # Generate Summary Report
        report = report_service.generate_report(enrollment_service.enrollments)
        print("\nSummary Report:")
        print(f"Total Enrollments: {report['total_enrollments']}")
        print(f"Unique Courses: {report['unique_courses']}")
        print(f"Unique Students: {report['unique_students']}")
        pause()

    elif choice == "7":  # Exit
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
        pause()