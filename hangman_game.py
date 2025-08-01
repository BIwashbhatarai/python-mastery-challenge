import random  # Importing random module to randomly choose a word

# Function to choose a random word from the list
def choose_random_word():
    word_list = ["hangman", "python", "challenge", "programming", "mastery", "project"]
    chosen_word = random.choice(word_list)  # Randomly pick one word
    return chosen_word

# Function to display the current guessed state of the word
def display_word(secret_word, guessed_letters):
    display = ''
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "  # Show the guessed letter
        else:
            display += "_ "  # Show an underscore for unguessed letters
    return display.strip()  # Remove extra space from the end

# Main game function
def play_hangman():
    print("Welcome to the Hangman game!")
    secret_word = choose_random_word()  # Choose a word to guess
    guessed_letters = []  # List to store letters guessed by the player
    attempts = 6  # Player can make 6 wrong guesses
    word_guessed = False  # Track if the word is fully guessed

    print(f"\nThe word has {len(secret_word)} letters. You have {attempts} wrong guesses.")
    print(display_word(secret_word, guessed_letters))  # Show initial blank word

    # Game loop
    while not word_guessed and attempts > 0:
        guess = input("\nEnter a letter: ").lower()  # Get user's guess

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        # Check if letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.append(guess)  # Add guess to guessed list

        # Check if guess is correct
        if guess in secret_word:
            print("✅ Good job! That letter is in the word.")
        else:
            attempts -= 1  # Wrong guess, reduce attempt
            print(f"❌ Sorry, wrong guess. Attempts left: {attempts}")

        current_display = display_word(secret_word, guessed_letters)  # Get current word status
        print(f"Current word: {current_display}")  # Show progress

        # Check if word is completely guessed
        if "_" not in current_display:
            word_guessed = True

    # End of game result
    if word_guessed:
        print(f"\n🎉 Congrats! You have guessed the word: {secret_word}")
    else:
        print(f"\n💀 Game over! The word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    play_hangman()
