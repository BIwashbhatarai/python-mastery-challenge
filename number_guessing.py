import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)  # Generate the number inside the function for encapsulation
    print("Welcome to the number guessing game!")
    print("Pick a number between 1 to 100.")
    
    attempts = 5
    print(f"You have total {attempts} attempts")
    
    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
            
            # Optional: Check if guess is within valid range
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue
            
            attempts -= 1  # Decrement attempts after valid guess
            
            if guess == number_to_guess:
                print("🎉 Congratulations! You have guessed the number.")
                break
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")
            
            print(f"Attempts left: {attempts}")
        
        except ValueError:
            print("Please enter a valid integer number.")
    
    else:  # This else corresponds to the while: executed if loop not broken (no correct guess)
        print(f"You ran out of attempts. The number was {number_to_guess}.")

number_guessing_game()
