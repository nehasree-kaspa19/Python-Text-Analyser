from collections import Counter
import re

def analyze_text(text):
    words = re.findall(r"\b[\w']+\b", text.lower())
    sentences = re.findall(r'[.!?]+', text)

    total_words = len(words)
    total_characters = len(text)
    total_sentences = len(sentences)

    average_word_length = (
        sum(len(word) for word in words) / total_words
        if total_words else 0
    )

    word_frequency = Counter(words)
    most_common_word = word_frequency.most_common(1)

    print("\n--- Text Analysis Results ---")
    print(f"Total words: {total_words}")
    print(f"Total characters: {total_characters}")
    print(f"Total sentences: {total_sentences}")
    print(f"Average word length: {average_word_length:.2f}")

    if most_common_word:
        print(f"Most frequent word: {most_common_word[0][0]}")
    else:
        print("Most frequent word: None")

text = input("Enter a paragraph to analyze:\n")
analyze_text(text)
