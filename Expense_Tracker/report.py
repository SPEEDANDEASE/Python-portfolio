from tracker import add_expense, summarise_expense, view_today_expenses

# Global shared data
categories = {
    "Food": {"items": [], "dates": []},
    "Transport": {"items": [], "dates": []},
    "Accommodation": {"items": [], "dates": []},
    "Data": {"items": [], "dates": []},
}

# Main menu loop
while True:
    try:
        response = int(input(
            "\nWelcome to Expense Tracker\n"
            "1. Add Expense\n"
            "2. View Today's Expenses\n"
            "3. View Summary\n"
            "4. Exit\nChoose: "
        ))
    except ValueError:
        print("Please enter a valid option (1–4).")
        continue

    if response == 1:
        categories = add_expense(categories)
    elif response == 2:
        view_today_expenses(categories)
    elif response == 3:
        summarise_expense(categories)
    elif response == 4:
        print("Goodbye. Keep tracking wisely!")
        break
    else:
        print("Invalid option. Try again.")
