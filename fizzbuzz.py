def fizzbuzz(n):
    for i in range(1, n + 1):  # Loop from 1 to n inclusive
        if i % 3 == 0 and i % 5 == 0:  # Divisible by both 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Divisible by 3 only
            print("Fizz")
        elif i % 5 == 0:  # Divisible by 5 only
            print("Buzz")
        else:
            print(i)

try:
    number = int(input("Enter the number up to which to run FizzBuzz: "))  # Prompt user input
    fizzbuzz(number)
except ValueError:
    print("Please enter a valid integer.")
