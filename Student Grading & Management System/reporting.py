def list_students(students):
    if not students:
        print("No students in the database yet.")
        return

    print("\n=== All Students ===")
    for student in students:
        print(f"Name: {student['name']} | ID: {student['id']}")
        for sub in student['subjects']:
            print(f"  Subject: {sub['subject']} | Score: {sub['score']} | Grade: {sub['grade']}")
        print("-" * 30)

def search_by_id(students):
    if not students:
        print("No students to search.")
        return

    search_id = input("Enter student ID to search: ")

    found = False
    for student in students:
        if student['id'] == search_id:
            print(f"Name: {student['name']} | ID: {student['id']}")
            for sub in student['subjects']:
                print(f"  Subject: {sub['subject']} | Score: {sub['score']} | Grade: {sub['grade']}")
            found = True
            break

    if not found:
        print(f"No student found with ID: {search_id}")
