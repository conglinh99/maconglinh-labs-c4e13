pair = 1
new_pair = 0
total = 0
month = int(input("Enter the number of month: "))
for i in range(month):
    total = pair + new_pair
    pair = total
    new_pair = pair
    print("Month {0}: {1} pair(s) of rabbit.".format(i, total))
