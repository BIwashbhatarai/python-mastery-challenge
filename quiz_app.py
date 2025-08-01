import json
import random

# Sample quiz data (can also be loaded from a file)
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"],
        "answer": "C"
    }
]

# Function to run the quiz
def run_quiz(questions):
    score = 0
    print("\n=== Welcome to the Quiz App ===\n")
    random.shuffle(questions)

    for idx, q in enumerate(questions, 1):
        print(f"Q{idx}: {q['question']}")
        for opt in q["options"]:
            print(opt)
        user_ans = input("Your answer (A/B/C/D): ").strip().upper()
        
        if user_ans == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")
    
    print(f"🎯 You scored {score} out of {len(questions)}")
    return score

# Function to save score
def save_score(username, score):
    score_file = "quiz_scores.json"

    try:
        with open(score_file, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    data[username] = score

    with open(score_file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"📁 Score saved for {username}!\n")

# Main function
def main():
    username = input("Enter your name: ").strip()
    score = run_quiz(questions)
    save_score(username, score)

if __name__ == "__main__":
    main()
