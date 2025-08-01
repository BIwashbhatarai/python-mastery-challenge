import os  # To work with file system (check if file exists)

CONTACT_FILE = "contacts.txt"  # File name where contacts will be stored

def add_contact():
    # Get contact details from user
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    
    # Open the file in append mode and add new contact
    with open(CONTACT_FILE, "a") as file:
        file.write(f"{name},{phone},{email}\n")  # Save contact in CSV format
    print("Contact added successfully!\n")

def view_contact():
    # Check if the contact file exists
    if not os.path.exists(CONTACT_FILE):
        print("No contact found.\n")
        return

    # Read all contacts from the file
    with open(CONTACT_FILE, "r") as file:
        contacts = file.readlines()

    if not contacts:
        print("No contact saved.\n")
    else:
        print("\nAll Contacts:")
        # Loop through each contact line
        for contact in contacts:
            parts = contact.strip().split(",")  # Split the line into name, phone, email
            if len(parts) == 3:
                name, phone, email = parts
                print(f"Name: {name} | Phone: {phone} | Email: {email}")  # Display contact
            else:
                print(f"Corrupted contact data: {contact}")  # Handle bad data gracefully
        print()

def search_contact():
    keyword = input("Enter name to search: ")
    found = False

    # Check if contacts file exists before searching
    if not os.path.exists(CONTACT_FILE):
        print("No contacts to search.\n")
        return

    # Search for contacts containing the keyword (case-insensitive)
    with open(CONTACT_FILE, "r") as file:
        for contact in file:
            parts = contact.strip().split(",")
            if len(parts) != 3:
                continue  # Skip corrupted lines
            name, phone, email = parts
            if keyword.lower() in name.lower():
                print(f"Found: Name: {name} | Phone: {phone} | Email: {email}")
                found = True

    if not found:
        print("No contact found with that name!")

def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ").lower()

    # Check if file exists before deleting
    if not os.path.exists(CONTACT_FILE):
        print("No contacts to delete.\n")
        return

    updated_contacts = []
    found = False

    # Read all contacts and filter out the one to delete
    with open(CONTACT_FILE, "r") as file:
        contacts = file.readlines()

    for contact in contacts:
        parts = contact.strip().split(",")
        if len(parts) != 3:
            continue  # Skip bad data
        name, phone, email = parts
        if name.lower() != name_to_delete:
            updated_contacts.append(contact)  # Keep other contacts
        else:
            found = True  # Mark that contact was found and removed

    # Write updated contact list back to file
    with open(CONTACT_FILE, "w") as file:
        file.writelines(updated_contacts)

    if found:
        print("Contact deleted successfully!\n")
    else:
        print("Contact not found.\n")

def contact_book():
    # Main menu loop to interact with user
    while True:
        print("Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_contact()  # Add a new contact
        elif choice == "2":
            view_contact()  # Show all contacts
        elif choice == "3":
            search_contact()  # Search contacts by name
        elif choice == "4":
            delete_contact()  # Delete a contact by name
        elif choice == "5":
            print("Exiting Contact Book. GoodBye!")
            break  # Exit the program
        else:
            print("Invalid Choice. Please try again.\n")  # Handle wrong input

# Run the contact book program only if this script is executed directly
if __name__ == "__main__":
    contact_book()
