numbers = []
words = []

# Input for numbers
while True:
    num = input("Enter a number (0 to stop): ")
    if num == '0':
        break
    try:
        numbers.append(int(num))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Input for words
while True:
    word = input("Enter a word (END to stop): ")
    if word == 'END':
        break
    if word.isalpha():
        words.append(word)
    else:
      print("Invalid input. Please enter a word with alphabetic characters only.")

# Sorting numbers and words
numbers_asc = sorted(numbers)
numbers_desc = sorted(numbers, reverse=True)
words_asc = sorted(words)
words_desc = sorted(words, reverse=True)

# Printing results
print("Numbers in ascending order:", numbers_asc)
print("Numbers in descending order:", numbers_desc)
print("Words in ascending order:", words_asc)
print("Words in descending order:", words_desc)
