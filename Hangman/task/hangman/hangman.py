# ---------------------------3---------------------------
# import random
#
# words = ['python', 'java', 'kotlin', 'javascript']
# word_needed = random.choice(words)
#
# print("Guess the word:")
# word_input = input()
# if word_needed == word_input:
#     print("You survived!")
# else:
#     print("You are hanged!")

# ---------------------------4---------------------------
import random

words = ['python', 'java', 'kotlin', 'javascript']
word_needed = random.choice(words)
hidden_word = word_needed[0:3] + '-' * (len(word_needed) - 3)

print(f"Guess the word: {hidden_word}")
word_input = input()
if word_needed == word_input:
    print("You survived!")
else:
    print("You are hanged!")