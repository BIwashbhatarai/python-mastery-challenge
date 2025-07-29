import random

def get_computer_choice():
    # Randomly select 'rock', 'paper', or 'scissors' for the computer
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    # Keep asking user until they enter a valid choice
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower().strip()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid choice. Please try again.")

def determine_winner(user, computer):
    # Decide winner based on user and computer choices
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    print("Welcome to Rock Paper Scissors!")
    while True:
        user_choice = get_user_choice()        # Get user input
        comp_choice = get_computer_choice()    # Get computer choice
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {comp_choice}")
        print(determine_winner(user_choice, comp_choice))  # Print the result

        # Ask if the user wants to play again
        play_again = input("Play again? (yes/no): ").lower().strip()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play()
