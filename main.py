import random

OPERATORS = ['x', '+', '-']
MAX_OPERANT = 12
MIN_OPERANT = 2

while True:
    left = random.randint(MIN_OPERANT, MAX_OPERANT)
    right = random.randint(MIN_OPERANT, MAX_OPERANT)
    middle = random.choice(OPERATORS)

    answer = input(f"{left} {middle} {right} = ")