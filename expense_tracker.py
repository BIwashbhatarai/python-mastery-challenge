import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

# Initialize CSV file with headers if it doesn't exist
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])

# Add a new expense
def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press enter for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    
    category = input("Enter category (e.g., Food, Transport, etc.): ")
    description = input("Enter description: ")
    
    try:
        amount = float(input("Enter amount: Rs. "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("✅ Expense added successfully!")

# View all expenses
def view_expenses():
    print("\nAll Expenses:")
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            print(f"{row[0]} | {row[1]} | {row[2]} | Rs.{row[3]}")

# View expenses by category
def view_by_category():
    category = input("Enter category to filter: ")
    total = 0
    print(f"\nExpenses in category: {category}")
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1].lower() == category.lower():
                print(f"{row[0]} | {row[2]} | Rs.{row[3]}")
                total += float(row[3])
    print(f"Total in '{category}': Rs.{total}")

# View monthly expense summary
def view_monthly_summary():
    month = input("Enter month (MM): ")
    year = input("Enter year (YYYY): ")
    total = 0
    print(f"\nExpenses for {month}/{year}:")
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            date = row[0]
            if date.startswith(f"{year}-{month}"):
                print(f"{row[0]} | {row[1]} | {row[2]} | Rs.{row[3]}")
                total += float(row[3])
    print(f"Total for {month}/{year}: Rs.{total}")

# Main menu
def main():
    initialize_file()
    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Expenses by Category")
        print("4. View Monthly Summary")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_by_category()
        elif choice == '4':
            view_monthly_summary()
        elif choice == '5':
            print("Goodbye! 🫡")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
