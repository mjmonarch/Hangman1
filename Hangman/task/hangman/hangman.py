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

# # ---------------------------5---------------------------
# import random
#
#
# def check_letter(_letter):
#     if letter not in word_needed:
#         return -1
#     count = word_needed.count(_letter)
#     start = 0
#     positions = []
#     for i in range(count):
#         position = word_needed.find(_letter, start)
#         start = position + 1
#         positions.append(position)
#     return positions
#
#
# # def tostr(text):
# #     _result = ""
# #     for _letter in text:
# #         _result.join(_letter)
# #     return _result
#
#
# words = ['python', 'java', 'kotlin', 'javascript']
# global word_needed
# word_needed = random.choice(words)
# hidden_word = list('-' * len(word_needed))
#
# print("H A N G M A N")
#
# tries = 8
# while tries > 0:
#     print()
#     print("".join(hidden_word))
#     print("Input a letter:")
#     letter = input()
#     result = check_letter(letter)
#     if result != -1:
#         for j in result:
#             hidden_word[j] = letter
#     else:
#         print("No such letter in the word")
#     tries -= 1
#
# print("""Thanks for playing!
# We'll see how well you did in the next stage""")

# ---------------------------6---------------------------
# import random
#
#
# def check_letter(_letter):
#     if letter not in word_needed:
#         return -1
#     if letter in letters_chosen:
#         return -2
#     letters_chosen.add(_letter)
#     count = word_needed.count(_letter)
#     start = 0
#     positions = []
#     for i in range(count):
#         position = word_needed.find(_letter, start)
#         start = position + 1
#         positions.append(position)
#     return positions
#
#
# words = ['python', 'java', 'kotlin', 'javascript']
#
# global word_needed
# global letters_chosen
# letters_chosen = set()
# word_needed = random.choice(words)
# hidden_word = list('-' * len(word_needed))
# letters_to_guess = len(set(word_needed))
#
# print("H A N G M A N")
#
# tries = 8
# while tries > 0:
#     print()
#     print("".join(hidden_word))
#     print("Input a letter: >")
#     letter = input()
#     result = check_letter(letter)
#     if result == -2:
#         tries -= 1
#         print("No improvements")
#     elif result == -1:
#         tries -= 1
#         print("No such letter in the word")
#     else:
#         for j in result:
#             hidden_word[j] = letter
#     if len(letters_chosen) == letters_to_guess:
#         print()
#         print("".join(hidden_word))
#         print("""You guessed the word!
# You survived!""")
#         break
# else:
#     print("You are hanged!")

# ---------------------------8---------------------------
#

import random


def check_letter(_letter):
    global letters_to_guess
    if len(_letter) > 1:
        return -4
    if not letter.islower():
        return -3
    if letter in letters_chosen:
        return -2
    if letter not in word_needed:
        letters_chosen.add(_letter)
        return -1
    letters_chosen.add(_letter)
    count = word_needed.count(_letter)
    start = 0
    positions = []
    for i in range(count):
        position = word_needed.find(_letter, start)
        start = position + 1
        positions.append(position)
    letters_to_guess -= 1
    return positions


words = ['python', 'java', 'kotlin', 'javascript']

global word_needed
global letters_chosen
global letters_to_guess

print("H A N G M A N")
while True:
    letters_chosen = set()
    word_needed = random.choice(words)
    letters_to_guess = len(set(word_needed))
    hidden_word = list('-' * len(word_needed))

    print('Type "play" to play the game, "exit" to quit:')
    choice = input()

    if choice == "exit":
        break
    if choice != "play":
        continue

    tries = 8
    while tries > 0:
        print()
        print("".join(hidden_word))
        print("Input a letter: >")
        letter = input()
        result = check_letter(letter)
        if result == -4:
            print("You should input a single letter")
        elif result == -3:
            print("It is not an ASCII lowercase letter")
        elif result == -2:
            print("You already typed this letter")
        elif result == -1:
            tries -= 1
            print("No such letter in the word")
        else:
            for j in result:
                hidden_word[j] = letter
        if letters_to_guess == 0:
            print()
            print("".join(hidden_word))
            print("""You guessed the word!
    You survived!
    """)
            break
    else:
        print("You are hanged!")
        print()
