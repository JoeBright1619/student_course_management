from ..models.report_base import ReportBase


class SummaryReport(ReportBase):
    def generate(self, enrollments):
        total = len(enrollments)
        courses = {e.course.course_code for e in enrollments}
        students = {e.student.student_id for e in enrollments}

        return {
            "total_enrollments": total,
            "unique_courses": len(courses),
            "unique_students": len(students),
        }
