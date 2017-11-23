def eval(x, y, operation):
    if operation == '+':
        print('x + y = ', int(x + y))
    elif operation == '-':
        print('x - y = ', int(x - y))
    elif operation == '/':
        print('x / y = ', x / y)
    elif operation == '*':
        print('x * y = ', int(x * y))
x = 10
y = 5
operation = '+'
r = eval(x, y, operation)
print(r)
    # return result
# s = eval()
# x = int(input('x = '))
# operation = input('operation: +, -, *, /')
# y = int(input('y = '))
# if operation in ['+', '-', '*', '/']:
#     r = eval()
#     #TODO: call even here
#
# else:
#     print('You have to type: "+, -, *, /"')
