"""
Requirements:

Inheritance

Polymorphism (e.g., different GPA rules, different reporting)

Overrides of methods if needed
    
"""

# models/undergraduate.py

from .student import Student

class Undergraduate(Student):
    """Student subtype that captures the current year level."""

    def __init__(self, student_id, name, email, level):
        """Extend the base constructor by persisting a class level."""
        super().__init__(student_id, name, email)
        self.level = level  # e.g. Year 1, 2, 3
