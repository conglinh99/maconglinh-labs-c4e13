bacteria = int(input("How many B bacterias are there? "))
time = int(input("How much time in minutes will we have wait?"))
times = 0
if time % 2 == 0:
    times = time/2
else:
    times = (time - 1)/2
total = bacteria * (2 ** times)
print("After {0} minutes, we would have {1} bacterias".format(time, total))
