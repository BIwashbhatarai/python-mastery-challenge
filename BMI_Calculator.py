# Function to calculate BMI using weight (kg) and height (cm)
def calculate_BMI(weight_KG, height_CM):
    height_m = height_CM / 100  # Convert cm to meters
    bmi = weight_KG / (height_m ** 2)  # BMI formula
    return bmi

# Function to classify BMI value into categories
def classify_BMI(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 24.9 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Main function to handle input/output and logic
def main():
    print("📊 BMI Calculator")

    try:
        # Take user input
        weight = float(input("Enter your weight in KG: "))
        height = float(input("Enter your height in CM: "))

        # Validate input
        if weight <= 0 or height <= 0:
            print("❌ Height and weight must be positive numbers!")
            return

        # Calculate BMI
        bmi = calculate_BMI(weight, height)
        category = classify_BMI(bmi)

        # Show result
        print(f"\n✅ Your BMI is: {bmi:.2f}")
        print(f"📋 Category: {category}")

    except ValueError:
        print("❌ Please enter valid numbers!")

# Entry point
if __name__ == "__main__":
    main()
