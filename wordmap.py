from collections import Counter
import matplotlib.pyplot as plt

# Sample messages
messages = ["india","india","Australia","Australia","Germany","Canada","Argentina","Australia","Australia"]

# Concatenate messages into a single string
text = ' '.join(messages)

# Split the text into words
words = text.split()

# Count the frequency of each word
word_counts = Counter(words)

# Create a word map
plt.bar(word_counts.keys(), word_counts.values())
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Word Map')
plt.show()
