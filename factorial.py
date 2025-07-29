def factorial(n):
    # Initialize result to 1 because factorial of 0 is 1
    result = 1
    # Loop from 1 to n to multiply all numbers
    for i in range(1, n + 1):
        result *= i  # Multiply result by current number i
    return result  # Return the final factorial value

try:
    # Take user input and convert to integer
    number = int(input("Enter a non-negative integer to find its factorial: "))
    # Check if number is negative
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Call factorial function and print the result
        print(f"The factorial of {number} is {factorial(number)}")
except ValueError:
    # Handle case where input is not an integer
    print("Please enter a valid integer.")
