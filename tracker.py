Delete tracker.py
from datetime import datetime

def add_expense(categories):
    while True:
        try:
            response = int(input(
                "\nCategory:\n1 - Food\n2 - Transport\n3 - Accommodation\n4 - Data\n5 - Exit\nChoose: "
            ))
        except ValueError:
            print("Enter a valid number between 1–5.")
            continue

        if response == 5:
            break

        category_map = {
            1: "Food",
            2: "Transport",
            3: "Accommodation",
            4: "Data"
        }

        if response in category_map:
            cat = category_map[response]
            item = input(f"Enter {cat} expense (e.g., 'Rice - 1500'): ")
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            if date == "":
                date = datetime.today().strftime("%Y-%m-%d")

            categories[cat]["items"].append(item)
            categories[cat]["dates"].append(date)
            print(f"{cat} expense added.")
        else:
            print("Invalid category choice.")
    return categories


def view_today_expenses(categories):
    today = datetime.today().strftime("%Y-%m-%d")
    print(f"\n🧾 Today's Expenses ({today}):")
    found = False
    for category, data in categories.items():
        for i, date in enumerate(data["dates"]):
            if date == today:
                print(f"{category}: {data['items'][i]}")
                found = True
    if not found:
        print("No expenses for today.")


def summarise_expense(categories):
    print("\n=== Expense Summary ===")
    for category, data in categories.items():
        print(f"\n{category}:")
        for item, date in zip(data["items"], data["dates"]):
            print(f"  {date} - {item}")
