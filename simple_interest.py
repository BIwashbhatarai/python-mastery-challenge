def simple_interest(principal, rate, time):
    """
    Calculate simple interest using the formula:
    Interest = (Principal × Rate × Time) / 100
    """
    interest = (principal * rate * time) / 100
    return interest

try:
    # Take user inputs and convert them to float
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    time = float(input("Enter the time period (in years): "))
    
    # Calculate simple interest
    interest = simple_interest(principal, rate, time)
    
    print(f"The simple interest is: {interest}")
except ValueError:
    print("Please enter valid numerical values.")
