numbers = [-100, -60, -45, 0, 3, 6, 15, 78]
start = 0
stop = len(numbers) - 1
found_index = -1
x = int(input("Enter a number?"))
while start != stop:
# for index, item in enumerate(numbers):
    mid = (start + stop)//2
    if x == numbers[mid]:
        found_index = mid
        break
    elif x < numbers[mid]:
        mid = (start + stop)//2
        stop = mid
    else:
        mid = (start + stop + 1)//2
        start = mid
if found_index == -1:
    print("Not found!")
else:
    print("Found at:", found_index + 1)
