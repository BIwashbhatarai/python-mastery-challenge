import datetime
import os
import nepali_datetime

FILE_NAME = "birthdays.txt"  # File to store birthdays

def nepali_to_gregorian(nep_date_str):
    """
    Convert Nepali BS date string (YYYY-MM-DD) to Gregorian AD date string.
    """
    try:
        # Convert string Nepali date to nepali_datetime.date object
        nep_date = nepali_datetime.date.fromisoformat(nep_date_str)
        # Convert Nepali date to Gregorian datetime.date object
        greg_date = nep_date.to_datetime_date()
        # Format Gregorian date as string YYYY-MM-DD
        return greg_date.strftime("%Y-%m-%d")
    except Exception:
        raise ValueError("Invalid Nepali date format or value.")

def view_date():
    # Ask user which date format to display
    format_choice = input("Which format do you want? (English or Nepali): ").lower()
    
    if format_choice == "english":
        english_date = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"Today's date is {english_date}")
    
    elif format_choice == "nepali":
        nepali_date = nepali_datetime.date.today()
        print(f"Today's date is {nepali_date}")
    
    else:
        print("Invalid format choice. Showing English date by default.")
        english_date = datetime.datetime.now().strftime("%Y-%m-%d")
        print(f"Today's date is {english_date}")

def add_birthday():
    # Get name input
    name = input("Enter name: ").strip()
    
    # Ask for date input format
    date_format = input("Enter birthday format? (AD for English, BS for Nepali): ").lower()

    # Get and convert date accordingly
    if date_format == 'bs':
        date_str = input("Enter birthday in Nepali BS (YYYY-MM-DD): ").strip()
        try:
            # Convert Nepali BS date to Gregorian AD string
            date_str = nepali_to_gregorian(date_str)
        except ValueError as e:
            print(f"❌ {e}")
            return
    else:
        date_str = input("Enter birthday in English AD (YYYY-MM-DD): ").strip()

    # Validate Gregorian date format
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format. Please use YYYY-MM-DD")
        return

    # Save birthday as Gregorian AD date
    with open(FILE_NAME, "a") as file:
        file.write(f"{name}, {date_str}\n")

    print(f"✅ Birthday for {name} added successfully!")

def view_birthday():
    # Check if file exists
    if not os.path.exists(FILE_NAME):
        print("No birthdays found yet!")
        return

    print("\n🎂 Saved Birthdays:")
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        if not lines:
            print("No birthdays saved yet!")
            return
        for line in lines:
            name, date = line.strip().split(",", 1)
            print(f"{name} - {date.strip()}")

def check_today_birthdays():
    # Get today's month and day in Gregorian AD
    today = datetime.datetime.now().strftime("%m-%d")
    found = False

    if not os.path.exists(FILE_NAME):
        print("No birthdays found.")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, date = line.strip().split(",", 1)
            date = date.strip()
            # Compare MM-DD part to today
            if date[5:] == today:
                print(f"🎉 Today is {name}'s birthday! 🎉")
                found = True

    if not found:
        print("No birthday today.")

def main():
    while True:
        print("\n--- Birthday Reminder ---")
        print("1. Add Birthday")
        print("2. View Birthdays")
        print("3. Check Today's Birthdays")
        print("4. Today's Date")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_birthday()
        elif choice == "2":
            view_birthday()
        elif choice == "3":
            check_today_birthdays()
        elif choice == "4":
            view_date()
        elif choice == "5":
            print("Goodbye! Enjoy your lunch! 🍽️")
            break
        else:
            print("Invalid choice, please choose option between 1-5")

if __name__ == "__main__":
    main()
