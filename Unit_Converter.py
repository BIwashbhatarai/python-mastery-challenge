# Function to convert length units
def convert_length():
    # Show available length units
    print("\nLength Units: meter, kilometer, mile, foot")
    
    # Get user input for source and target units
    from_unit = input("Convert from: ").lower()
    to_unit = input("Convert to: ").lower()

    # Get the value to convert and handle non-numeric input
    try:
        value = float(input("Enter value: "))
    except ValueError:
        print("Invalid number!")  # Show error if input is not a number
        return  # Exit function early

    # Conversion factors relative to 1 meter
    length_factors = {
        'meter': 1,
        'kilometer': 1000.0,
        'mile': 1609.34,
        'foot': 0.3048
    }

    # Check if both units are valid
    if from_unit not in length_factors or to_unit not in length_factors:
        print("Invalid unit selected.")
        return

    # Convert value: from original → meters → target unit
    result = value * length_factors[from_unit] / length_factors[to_unit]

    # Display final result
    print(f"\n✅ {value} {from_unit} = {result:.4f} {to_unit}")


# Function to convert weight units
def convert_weight():
    # Show available weight units
    print("\nWeight Units: gram, kilogram, pound, ounce")

    # Get user input for source and target units
    from_unit = input("Convert from: ").lower()
    to_unit = input("Convert to: ").lower()

    # Get the value to convert and handle invalid number input
    try:
        value = float(input("Enter value: "))
    except ValueError:
        print("Invalid number!")  # Show error if input is not a number
        return  # Exit function early

    # Conversion factors relative to 1 gram
    weight_factors = {
        'gram': 1,
        'kilogram': 1000.0,
        'pound': 453.592,
        'ounce': 28.3495
    }

    # Check if both units are valid
    if from_unit not in weight_factors or to_unit not in weight_factors:
        print("Invalid unit selected.")
        return

    # Convert value: from original → grams → target unit
    result = value * weight_factors[from_unit] / weight_factors[to_unit]

    # Display final result
    print(f"\n✅ {value} {from_unit} = {result:.4f} {to_unit}")


# Main function to run the converter
def main():
    # Run until the user chooses to exit
    while True:
        # Show main menu
        print(f"\n--- Unit Converter ----")
        print("1. Convert Length")
        print("2. Convert Weight")
        print("3. Exit")

        # Get user's choice
        choice = input("Enter your choice (1-3): ")

        # Perform action based on choice
        if choice == "1":
            convert_length()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            print("Goodbye! 👋")  # Exit message
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please choose between 1-3.")  # Handle wrong input

# Run the main function only when this script is executed directly
if __name__ == "__main__":
    main()
