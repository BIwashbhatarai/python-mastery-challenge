import re
import random 

rules = {
    r'hi|hello|hey': [
        "Hello there!", "Hi! How can I help you!", "Hey! Good to see you!"
    ],
    r'how are you | how are you doing': [
        "I'm just a bunch of code, but I'm doing fine!",
        "All systems go! what about you?"
    ],
    r'bye|goodbye|see you':[
        "Goodbye! Have a great day!",
        "See you later!",
        "Bye-Bye"
    ],
    r'help|can you help me': [
        "Of couse! I'm here to help. What do you need?",
        "Sure! Just tell me what you're looking for."
    ]
}

default_responses = [
    "I'm not sure I understand that.",
    "Can you rephrase that? ",
    "Hmm... I don't know how to respond to that"
]

def get_response(user_input):
    user_input = user_input.lower()
    for pattern , responses in rules.items():
        if re.search(pattern, user_input):
            return random.choice(responses)
    return random.choice(default_responses)

print("🤖 PyBot: Hello! Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("🤖 PyBot: Chat ended. Bye!")
        break
    response = get_response(user_input)
    print("🤖 PyBot: ", response)