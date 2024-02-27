import random
import time

OPERATORS = ['*', '+', '-']
MAX_OPERANT = 12
MIN_OPERANT = 2

def que_ans_generator():
    left = random.randint(MIN_OPERANT, MAX_OPERANT)
    right = random.randint(MIN_OPERANT, MAX_OPERANT)
    middle = random.choice(OPERATORS)

    exp = f"{left} {middle} {right}"
    ans = eval(exp)
    # this is the python fn that solves simple maths problems and store the answer.
    return exp, ans

problem_num = 1
correct_count = 0
input("PRESS ENTER TO START\n---------------------")
while True:
        exp, ans = que_ans_generator()
        print(f"Problem #{problem_num}:")
        print("Press 'q' to quit.") 
        user_input = input(f"{exp} = ")
        if user_input == str(ans):
            print("Correct")
            correct_count += 1
        elif user_input == 'q':
            print(f"You scored {correct_count} out of {problem_num - 1}.")
            print("---------------------")
            quit()
        else: print("Wrong")
        
        problem_num += 1

    