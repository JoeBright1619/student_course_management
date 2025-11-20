"""
Requirements:

Abstract Base Class (ABC)

Polymorphism

"""

# models/report_base.py

from abc import ABC, abstractmethod

class ReportBase(ABC):

    @abstractmethod
    def generate_report(self):
        pass
