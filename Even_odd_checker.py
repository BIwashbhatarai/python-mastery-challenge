def even_odd_check(num):
    # Check if the number is divisible by 2
    if num % 2 == 0:
        return f"The number {num} is Even"
    return f"The number {num} is Odd"

try:
    # Take user input and convert to integer
    number = int(input("Enter a number: "))
    # Call the function and print the result
    print(even_odd_check(number))
except ValueError:
    # Handle invalid input that can't be converted to int
    print("Please enter a valid integer number.")
