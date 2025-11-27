"""Contains:

Formatting helpers

JSON saving/loading (optional)

Utility shortcuts"""

def format_student(student):
    """Return a consistent string rendering for student listings."""
    return f"{student.student_id} | {student.name} | {student.email}"

def format_course(course):
    """Return a consistent string rendering for course listings."""
    return f"{course.course_code} | {course.title}"
