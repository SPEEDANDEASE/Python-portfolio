def add_student():
    student = {}
    student['name'] = input("Enter student full name: ")

    student['id'] = input("Enter student ID: ")

    student['subjects'] = []

    while True:
        try:
            s = int(input("Enter:\n1 to add subject & score\n2 to stop adding subjects\n"))
        except ValueError:
            print("Input must be 1 or 2.")
            continue

        if s == 2:
            break

        subject = input("Enter subject: ")

        try:
            score = int(input("Enter score: "))
        except ValueError:
            print("Score must be a number.")
            continue

        if score >= 70:
            grade = "A"
        elif score >= 60:
            grade = "B"
        elif score >= 50:
            grade = "C"
        elif score >= 40:
            grade = "D"
        elif score >= 30:
            grade = "E"
        else:
            grade = "F"

        student['subjects'].append({
            "subject": subject,
            "score": score,
            "grade": grade
        })

    return student
