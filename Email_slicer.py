# Function to split email into username and domain parts
def slice_Email(email):
    # Check if '@' is present in the email string
    if "@" not in email:
        return None, None  # Invalid email format
    
    # Split email into username and domain at the first '@'
    username, domain = email.split("@", 1)
    return username, domain

def main():
    print("📧 Email Slicer")
    
    # Take email input from the user, remove extra spaces
    email = input("Enter your Email: ").strip()
    
    # Get username and domain from the email slicer function
    username, domain = slice_Email(email)
    
    # Validate and print results or error message
    if username and domain:
        print(f"Username: {username}")
        print(f"Domain: {domain}")
    else:
        print("❌ Invalid Email format. Please enter a valid Email.")
        
# Program entry point
if __name__ == "__main__":
    main()
