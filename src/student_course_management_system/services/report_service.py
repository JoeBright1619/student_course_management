from ..models.report_base import ReportBase

class SummaryReport(ReportBase):
    def generate_report(self, enrollments):

        total = len(enrollments)
        course_info = {(e.course.course_code, e.course.title) for e in enrollments}
        students = {e.student.student_id for e in enrollments}

        course_averages = {}

        
        for code, name in course_info:
            scores = [
                float(e.score)
                for e in enrollments
                if e.course.course_code == code and e.score is not None
            ]
            if scores:
                course_averages[name] = sum(scores) / len(scores)

        formatted_avg = "".join(
            f"\n{course_name} | {avg:.2f}" for course_name, avg in course_averages.items()
        )


        return {
            "total_enrollments": total,
            "unique_courses": len(course_info),
            "unique_students": len(students),
            "course_averages": "\nCourse_name  |  score"+formatted_avg,
        }
