## Student Course Management System

Command-line tool for managing students, courses, enrollments, grades, and summary
reports. The app uses a clean separation of concerns with models, services, and
utility layers orchestrated by `main.py`.

### Features

- Menu-driven CLI for quick data entry
- Supports undergraduate and graduate student types
- Course catalog management
- Student-to-course enrollment tracking
- Grade recording with validation helpers
- Summary reporting across enrollments, courses, and students

### Project Layout

- `main.py`: CLI entry point that wires menus to the service layer
- `src/student_course_management_system/models`: Domain objects such as
  `Student`, `Undergraduate`, `Graduate`, `Course`, and `enrollment abstractions`
- `src/student_course_management_system/services`: Business logic for students,
  courses, enrollments, and reporting
- `src/student_course_management_system/utils`: Menus and input validation helpers

### Requirements

- Python 3.13+
- [Poetry](https://python-poetry.org/) for dependency management

### Setup

```bash
poetry install
```

### Running the App

```bash
poetry run python main.py
```

Follow the on-screen numbered menu to add students, create courses, enroll
students, record grades, and generate summary reports.

### Notes

- Data is stored in memory; restart the CLI to reset the state.
- Email, numeric IDs, and score inputs use the validation helpers in
  `src/student_course_management_system/utils/input_handlers.py`.
