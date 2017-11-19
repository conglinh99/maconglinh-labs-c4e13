pair = 1
new_pair = 0
total = 0
month = int(input("Enter the number of month: "))
for i in range(month + 1):
    total = pair + new_pair
    new_pair = pair
    pair = total
    print("Month {0}: {1} pair(s) of rabbit.".format(i, total))
