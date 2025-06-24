print("=== STUDENT GRADE REPORT GENERATOR ===")

names = []
scores = []
grades = []

total = 0
count = 0

while True:
    student_name = input("Enter student name: ").strip()
    try:
        student_score = int(input("Enter student score (0–100): "))
    except ValueError:
        print("Invalid input. Score must be a number.")
        continue

    # Save student data
    names.append(student_name)
    scores.append(student_score)
    count += 1
    total += student_score

    # Determine grade
    if student_score >= 70:
        grade = 'A'
    elif student_score >= 60:
        grade = 'B'
    elif student_score >= 50:
        grade = 'C'
    elif student_score >= 40:
        grade = 'D'
    elif student_score >= 30:
        grade = 'E'
    else:
        grade = 'F'
    grades.append(grade)

    print(f"{student_name} got a grade of {grade}.")

    # Ask if user wants to continue
    choice = input("Do you want to enter another student? (yes/no): ").strip().lower()
    if choice != "yes":
        break

# Final report
print("\n--- GRADE REPORT ---")
for i in range(count):
    print(f"{names[i]}: Score = {scores[i]}, Grade = {grades[i]}")

if count > 0:
    average = total / count
    print(f"\nTotal score of all students: {total}")
    print(f"Average score: {average:.2f}")
else:
    print("No student data entered.")
add grade_report.py
