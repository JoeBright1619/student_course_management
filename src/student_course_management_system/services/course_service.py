"""
Requirements:

More control flow

Filtering with list comprehensions

"""

from ..models.course import Course


class CourseService:
    """Encapsulates create/read helpers for `Course` objects."""

    def __init__(self):
        self.courses = {}  # key: course_code, value: Course object

    def add_course(self, *args, **kwargs):
        """Instantiate and store a new course, enforcing unique codes."""
        course = Course(*args, **kwargs)

        if course.course_code in self.courses:
            raise ValueError("Course exists")

        self.courses[course.course_code] = course
        return course

    def get_course(self, id):
        """Fetch a course by code; returns `None` when missing."""
        return self.courses.get(id)

    def list_courses(self):
        """Return all courses as a list for easier iteration."""
        return list(self.courses.values())

    def search_courses(self, keyword):
        """Simple case-insensitive substring search across course titles."""
        return [
            c for c in self.courses.values()
            if keyword.lower() in c.title.lower()
        ]
