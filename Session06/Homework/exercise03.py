from turtle import *
length = int(input("Enter the length of square: "))
color = input("Enter the color of square: ")
def draw_square(length, color):
    for i in range(4):
        pencolor(color)
        forward(length)
        left(90)
draw_square(length, color)
mainloop()
