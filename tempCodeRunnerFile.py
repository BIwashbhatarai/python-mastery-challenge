def count_word(text):
    words = text.strip().split()
    return len(words)

text = input("Enter a sentence or a paragraph")
word_count = count_word(text)
print(f"Total words: {word_count}")