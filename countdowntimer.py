import time  # Imports the time module to use the sleep function

# Defines the countdown function that takes the total seconds as input
def countdown(seconds):
    while seconds > 0:  # Continue looping until the countdown reaches 0
        print(f"Time left: {seconds} seconds")  # Display remaining time
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Decrease seconds by 1
    print("Time's up!")  # Message when countdown ends

# Main logic starts here
try:
    # Ask the user to input time in seconds and convert to integer
    seconds = int(input("Enter time in seconds: "))
    countdown(seconds)  # Call the countdown function
except ValueError:
    # Handle non-integer input gracefully
    print("Please enter a valid integer value.")
