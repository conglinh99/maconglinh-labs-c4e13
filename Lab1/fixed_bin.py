numbers = [-100, -20, 0, 11, 20, 40]
start = 0
stop = len(numbers)
x = int(input("Enter a number?"))
found_index = -1
while start != stop:
    mid = (start + stop)// 2
    if x == numbers[mid]:
        found_index = mid
        break
    else:
        if mid == star or mid == stop:
            break
        elif x < numbers[mid]:
            stop = mid
        else:
            start = mid
if found_index == -1:
    print("Not found!")
else:
    print("Found at: ", found_index)
