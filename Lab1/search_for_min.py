numbers = [10, 5, 7, -19, -40, 59, 37]
min_number = numbers[0]
max_number = numbers[0]
for i in numbers:
    if min_number > i:
        min_number = i
    if max_number < i:
        max_number = i
print("Min:", min_number)
print("Max:", max_number)
