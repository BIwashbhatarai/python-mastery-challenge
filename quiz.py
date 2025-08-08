quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) Charles Dickens", "B) Mark Twain", "C) William Shakespeare", "D) Leo Tolstoy"],
        "answer": "C"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A) Elephant", "B) Giraffe", "C) Blue Whale", "D) Hippopotamus"],
        "answer": "C"
    },
    {
        "question": "Which language is used to create Android Apps?",
        "options": ["A) Java", "B) C++", "C) Python", "D) Kotlin"],
        "answer": "A"
    }
]

def run_quiz():
    score = 0
    print("\n---Welcome to the Quiz App---\n")
    
    for index, question in enumerate(quiz_data, start=1):
        print(f"Q.{index}: {question['question']}")
        for option in question['options']:
            print(option)
        userInput = input("\nEnter your option: ").strip().upper()
        if userInput == question['answer']:
            print("✅ That's Correct!")
            score += 1
        else:
            print(f"❌ That's Incorrect!, The correct answer was {question['answer']}")
    print(f"Your final score : {score} out of {len(quiz_data)}")

    play_again = input("Do you wanna play again (yes/no): ").strip().lower()
    if play_again in ["yes", 'y']:
        run_quiz()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    run_quiz()