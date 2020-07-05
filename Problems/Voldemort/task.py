import random


# work with this variable
n = int(input())

random.seed(n)
name = "Voldemort"

print(random.choice(name))
