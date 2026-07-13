#Word Frequency Counter
'''Problem Statement: Accept a sentence from the user and create a dictionary that stores the frequency of each word.
Example:
Input: python is easy and python is powerful Output: { 'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1 }
Additionally:
•
Display the most frequently occurring word.
•
Display all words in alphabetical order.'''
#-----------------------------------coding----------------------------------------------
# Accept a sentence from the user
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

# Create dictionary to store word frequencies
word_freq = {}

for word in words:
    word = word.lower()   # make case-insensitive
    word_freq[word] = word_freq.get(word, 0) + 1

# Display the dictionary
print("\nWord Frequency Dictionary:")
print(word_freq)

# Display the most frequently occurring word
most_frequent = max(word_freq, key=word_freq.get)
print(f"\nMost frequent word: '{most_frequent}' (occurs {word_freq[most_frequent]} times)")

# Display all words in alphabetical order
print("\nWords in alphabetical order:")
for word in sorted(word_freq.keys()):
    print(f"{word}: {word_freq[word]}")
#------------------------------------------------------------------------------------
'''output:
Enter a sentence: python is easy and python is powerful
Word Frequency Dictionary:
{'python': 2, 'is': 2, 'easy': 1, 'and': 1, 'powerful': 1}

Most frequent word: 'python' (occurs 2 times)

Words in alphabetical order:
and: 1
easy: 1
is: 2
powerful: 1
python: 2
'''