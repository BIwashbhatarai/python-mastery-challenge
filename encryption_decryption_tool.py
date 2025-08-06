from cryptography.fernet import Fernet
import os

# ---------------------- Generate or Load Key ---------------------- #

# This function generates a new encryption key and saves it in 'secret.key'
def generate_key():
    key = Fernet.generate_key()  # Generate a secure random key
    with open("secret.key", "wb") as key_file:
        key_file.write(key)       # Save key to a file for later use
    print("🔑 Key generated and saved as 'secret.key'")

# This function loads the key from the 'secret.key' file
def load_key():
    if not os.path.exists("secret.key"):
        print("❌ Key not found. Please generate one first.")
        return None
    with open("secret.key", "rb") as key_file:
        return key_file.read()  # Read and return the key

# ---------------------- Encrypt Function ---------------------- #

# Encrypts the contents of a given file using the loaded key
def encrypt_file(filename):
    key = load_key()
    if key is None: return  # If no key found, exit the function

    f = Fernet(key)  # Create Fernet object with the key
    try:
        with open(filename, "rb") as file:
            data = file.read()     # Read the file contents (as bytes)
        encrypted = f.encrypt(data)  # Encrypt the data
        with open(filename, "wb") as file:
            file.write(encrypted)  # Overwrite the file with encrypted data
        print(f"✅ File '{filename}' encrypted.")
    except FileNotFoundError:
        print("❌ File not found.")

# ---------------------- Decrypt Function ---------------------- #

# Decrypts the contents of a file encrypted using Fernet
def decrypt_file(filename):
    key = load_key()
    if key is None: return

    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            data = file.read()     # Read the encrypted data
        decrypted = f.decrypt(data)  # Decrypt the data
        with open(filename, "wb") as file:
            file.write(decrypted)  # Write decrypted data back to file
        print(f"🔓 File '{filename}' decrypted.")
    except FileNotFoundError:
        print("❌ File not found.")
    except Exception as e:
        # In case the file is already decrypted or key is invalid
        print("❌ Decryption failed:", str(e))

# ---------------------- CLI Menu ---------------------- #

# Shows menu to the user and takes input to run operations
def menu():
    while True:
        print("\n🔐 File Encryption Tool")
        print("1. Generate Key")
        print("2. Encrypt File")
        print("3. Decrypt File")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            generate_key()  # Option 1: Generate a new key
        elif choice == "2":
            filename = input("Enter filename to encrypt: ")
            encrypt_file(filename)  # Option 2: Encrypt a file
        elif choice == "3":
            filename = input("Enter filename to decrypt: ")
            decrypt_file(filename)  # Option 3: Decrypt a file
        elif choice == "4":
            print("👋 Exiting...")
            break  # Exit the loop and program
        else:
            print("❌ Invalid choice. Try again.")

# ---------------------- Main Program Entry ---------------------- #

# Start the app by calling menu()
if __name__ == "__main__":
    menu()
