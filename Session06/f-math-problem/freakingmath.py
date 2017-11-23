from random import *

def generate_quiz():
    x = randint(1, 10)
    y = randint(1, 10)
    op = choice(['+', '-', '*', '/'])
    error = randint(-5, 5)
    true_result = int(eval("{0} {1} {2}".format(x, op, y)))
    result = true_result + error
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    true_result = int(eval("{0} {1} {2}".format(x,op,y)))
    if user_choice:
        return true_result == result
    else:
        return true_result != result
