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
# import random
#
# words = ['python', 'java', 'kotlin', 'javascript']
# word_needed = random.choice(words)
# hidden_word = word_needed[0:3] + '-' * (len(word_needed) - 3)
#
# print(f"Guess the word: {hidden_word}")
# word_input = input()
# if word_needed == word_input:
#     print("You survived!")
# else:
#     print("You are hanged!")

# ---------------------------5---------------------------
import random


def check_letter(_letter):
    if letter not in word_needed:
        return -1
    count = word_needed.count(_letter)
    start = 0
    positions = []
    for i in range(count):
        position = word_needed.find(_letter, start)
        start = position + 1
        positions.append(position)
    return positions


# def tostr(text):
#     _result = ""
#     for _letter in text:
#         _result.join(_letter)
#     return _result


words = ['python', 'java', 'kotlin', 'javascript']
global word_needed
word_needed = random.choice(words)
hidden_word = list('-' * len(word_needed))

# print("H A N G M A N")
tries = 8
while tries > 0:
    print("".join(hidden_word))
    print("Input a letter:")
    letter = input()
    result = check_letter(letter)
    if result != -1:
        for j in result:
            hidden_word[j] = letter
    else:
        print("No such letter in the word")
    tries -= 1

print("""Thanks for playing!
We'll see how well you did in the next stage""")
