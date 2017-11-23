from turtle import *

print("Enter the start position of the star(x, y):")
x = int(input('x = '))
y = int(input('y = '))
length = int(input("Enter the length of star's side: "))

def draw_star(x, y, length):
    left(36)
    up()
    setposition(x,y)
    down()
    for i in range(5):
        forward(length)
        left(144)
draw_star(x, y, length)
mainloop()
