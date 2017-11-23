from random import randint
while True:
    x = randint(0, 10)
    y = randint(0, 10)
    error = randint(-1, 1)
    op = ['+','-','*','/']
    op_ = random.choice(op)
    answer = (x op_ y)
    result = (x op_ y) + error
    print("*"*10)
    print("{0} {1} {2} = {3}".format(x, y, op_random, result))
    print('*'*10)
    guess = input("(Y/N)?").upper()
    if answer == result:
        if guess == 'Y':
            print("Exactly!")
        else:
            print('Oh!Shit =))')
    if answer != result:
        if guess == 'Y':
            print('Oh!Shit =))')
        else:
            print('Exactly!')
