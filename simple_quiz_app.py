def quiz_game():
    # List of questions with their corresponding answers stored as dictionaries
    questions = [
        {
            "question": "What is the capital of France?",  # Question text
            "answer": "paris"                              # Correct answer (lowercase)
        },
        {
            "question": "What is 5 + 7?",                  # Question text
            "answer": "12"                                 # Correct answer as string
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",  # Question text
            "answer": "shakespeare"                        # Correct answer (lowercase)
        }
    ]

    score = 0  # Initialize user's score to zero

    # Loop through each question in the list
    for q in questions:
        # Prompt user for an answer; strip whitespace and convert to lowercase for case-insensitive comparison
        user_answer = input(q["question"] + " ").strip().lower()
        
        # Check if user's answer matches the correct answer
        if user_answer == q["answer"]:
            print("Correct!")  # Inform user the answer is correct
            score += 1         # Increment score by 1
        else:
            # Inform user the answer was wrong and display the correct answer (capitalized for neatness)
            print(f"Wrong! The correct answer is {q['answer'].capitalize()}.")

    # After all questions, display the final score out of total questions
    print(f"\nYour final score is {score} out of {len(questions)}.")

# Runs the quiz game only if this script is executed directly (not imported)
if __name__ == "__main__":
    quiz_game()
