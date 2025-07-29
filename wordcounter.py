def count_word(text):
    # Remove leading/trailing spaces and split the text into words by whitespace
    words = text.strip().split()
    # Return the number of words
    return len(words)

# Ask user to enter a sentence or paragraph
text = input("Enter a sentence or a paragraph: ")

# Call the count_word function to count words in the input
word_count = count_word(text)

# Print the total number of words
print(f"Total words: {word_count}")
