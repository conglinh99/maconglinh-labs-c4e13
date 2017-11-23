from random import randint, choice
from calc import eval

def f_math(x, y, op, error):
    x = randint(0, 10)
    y = randint(0, 10)
    op = choice (['+', '-', '*', '/'])
    error = randint(-1, 1)
    true_result = eval(x, y, op)
    result = eval(true_result, error, op)
    
print("{0} {3} {1} = {2}".format(x, y, result, op))

# choice = input('Y/N').lower()
# if choice == 'y':
#     if error == 0:
#         print('Yay')
#     else:
#         print('Wrong:(')
# else:
#     if error != 0:
#         print('Wrong :(')
#     else:
#         print('Yay')
