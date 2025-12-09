"""
Contains:

Safe input functions

Number validation

String validation

Reusable CLI prompts

Purpose: Keep main.py clean.
"""


# utils/validators.py

def is_valid_email(email):
    """Simple check for valid email format."""
    return "@" in email and "." in email

def is_valid_int(value):
    """Check if input can be converted to integer."""
    try:
        int(value)
        return True
    except ValueError:
        return False

def is_valid_score(value):
    """Ensure a numeric input falls within the 0-100 range."""
    try:
        value = float(value)
        return value >= 0 and value <= 100
    except ValueError:
        return False
def is_valid_year(value):
    try:
        if int(value) > 1 and int(value) < 4:
            return True
        return False
    except ValueError:
        return False
def is_non_empty_string(value):
    """Check if a string is not empty."""
    return isinstance(value, str) and value.strip() != ""
