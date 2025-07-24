# Simulates a student management system where you can add student records, assign scores, compute grades, and generate reports.
#
# Dictionaries: To hold each student’s info (name, ID, scores)
# Functions: To add students, calculate GPA, and search records
# Modules: main.py, student_utils.py, reporting.py
# Sets: To prevent duplicate student IDs
# Loop logic: For menu and data entry
#
# 1. Add New Student
# 2. Enter Scores
# 3. Generate Report Card
# 4. List All Students
# 5. Search by ID

from student_utils import add_student
from reporting import list_students, search_by_id

students = []

print("=== Student Database & Grading System ===")

while True:
    try:
        response = int(input("""
1. Add New Student
2. List All Students
3. Search by ID
4. Exit
Enter option: """))
    except ValueError:
        print("Use numbers only (1-4).")
        continue

    if response == 1:
        student = add_student()
        students.append(student)
        print("Student added successfully!\n")

    elif response == 2:
        list_students(students)

    elif response == 3:
        search_by_id(students)

    elif response == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
