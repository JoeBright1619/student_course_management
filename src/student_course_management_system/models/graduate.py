"""
Requirements:

Inheritance

Polymorphism (e.g., different GPA rules, different reporting)

Overrides of methods if needed
    
"""


# models/graduate.py

from .student import Student

class Graduate(Student):
    def __init__(self, student_id, name, email, thesis_topic):
        super().__init__(student_id, name, email)
        self.thesis_topic = thesis_topic
