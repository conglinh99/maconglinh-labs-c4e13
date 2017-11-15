numbers = [1, 2, 6, -100, 50, -5, 35]
n = int(input("Enter a number?"))
found_index = -1
for index, item in enumerate(numbers):
    if n == item:
        found_index = index
        break
if found_index == -1:
    print("Not found!")
else:
    print("Found at: ", found_index + 1)
