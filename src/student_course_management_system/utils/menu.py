# utils/menu.py

def main_menu():
    print("\n=== Student Course Management System ===")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student in Course")
    print("4. Record Student score in a Course")
    print("5. View Students")
    print("6. View Courses")
    print("7. Generate Summary Report")
    print("8. Exit")
    
    choice = input("Enter your choice: ")
    return choice


def pause():
    input("\nPress Enter to continue...")


def student_type_menu():
    print("\nSelect Student Type:")
    print("1. Undergraduate")
    print("2. Graduate")
    choice = input("Enter choice: ")
    return choice
