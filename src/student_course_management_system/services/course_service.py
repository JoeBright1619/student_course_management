"""
Requirements:

More control flow

Filtering with list comprehensions

"""

from ..models.course import Course


class CourseService:
    def __init__(self):
        self.courses = {}  # key: course_code, value: Course object

    def add_course(self, *args, **kwargs):
        course = Course(*args, **kwargs)

        if course.course_code in self.courses:
            raise ValueError("Course exists")

        self.courses[course.course_code] = course
        return course

    def get_course(self, id):
        return self.courses.get(id)

    def list_courses(self):
        return list(self.courses.values())

    def search_courses(self, keyword):
        return [
            c for c in self.courses.values()
            if keyword.lower() in c.title.lower()
        ]
