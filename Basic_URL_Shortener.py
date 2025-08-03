import string
import random

# Dictionary to store short_code -> original URL
url_mapping = {}

# Function to generate a random short code of given length
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits  # a-zA-Z0-9
    short_code = ""
    for _ in range(length):
        short_code += random.choice(characters)
    return short_code

# Function to shorten a URL and store it with a unique short code
def shorten_url(long_url):
    while True:
        short_code = generate_short_code()
        if short_code not in url_mapping:
            url_mapping[short_code] = long_url
            return short_code

# Function to retrieve the original URL by short code
def retrieve_url(short_code):
    return url_mapping.get(short_code)

# Main program loop
def main():
    print("🔗 Basic URL Shortener")

    while True:
        # Display menu options
        print("\nOptions:")
        print("1. Shorten a URL")
        print("2. Retrieve a URL by short code")
        print("3. Exit")  # Fixed menu option

        # Get user input
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            # Shorten a new URL
            long_url = input("Enter the URL to shorten: ").strip()
            short_code = shorten_url(long_url)
            print(f"Shortened URL: {short_code}")

        elif choice == "2":
            # Retrieve original URL by code
            code = input("Enter the short code: ").strip()
            original_URL = retrieve_url(code)
            if original_URL:
                print(f"Original URL: {original_URL}")
            else:
                print("❌ No short code found")

        elif choice == "3":
            # Exit the program
            print("Goodbye 👋")
            break

        else:
            print("❌ Invalid choice. Please select 1, 2 or 3")

# Entry point of the program
if __name__ == "__main__":
    main()
