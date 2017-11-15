numbers = [-100, -50, 70, 1, 2, 5, -70, -50, 3, 5, -20, -100, 1, 2]
print("number = ", numbers)

#without using count()
count = 0
x = int(input("Enter a number? "))
for index, item in enumerate(numbers):
    if x == item:
        count += 1
print("{0} appears {1} time(s) in my list".format(x, count))

#using count()
counts = numbers.count(x)
print("{0} appears {1} time(s) in my list".format(x, counts))
