"""
Requirements:

Abstract Base Class (ABC)

Polymorphism

"""

# models/report_base.py

from abc import ABC, abstractmethod

class ReportBase(ABC):
    """Common interface for all reporting strategies."""

    @abstractmethod
    def generate_report(self):
        """Return a dictionary (or serializable structure) summarizing data."""
        pass
