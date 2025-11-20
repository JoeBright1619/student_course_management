"""Contains:

Formatting helpers

JSON saving/loading (optional)

Utility shortcuts"""

def format_student(student):
    return f"{student.student_id} | {student.name} | {student.email}"

def format_course(course):
    return f"{course.course_code} | {course.title}"
