n = int(input("Enter a number: "))
i = 2
loop_continue = True
if n == 2:
    loop_continue = True
elif n > 2:
    while i <= int(n**0.5):
        if n % i == 0:
            loop_continue = False
            break
        i+= 1
else:
    loop_continue = False
if loop_continue == True:
    print(n, " is a prime number")
else:
    print(n, "is not a prime number")
