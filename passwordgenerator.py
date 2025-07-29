import random
import string

# Function to generate a random password of given length
def generate_password(length):
    # Combine uppercase, lowercase, digits, and symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    
    # Pick a random character from the combined set for each position
    for _ in range(length):
        password += random.choice(characters)
        
    return password

try:
    # Get user input for password length
    length = int(input("Enter the password length: "))
    
    # Check for valid length
    if length < 0:
        print("Password length must be positive.")
    else:
        # Generate and display the password
        print(f"Generated Password: {generate_password(length)}")
        
except ValueError:
    # Handle non-integer input
    print("Please enter a valid number.")
