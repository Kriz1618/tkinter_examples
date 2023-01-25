import turtle
turtle.bgcolor("black")
turtle.pensize(1)
turtle.speed(0.1)
colours = ["green","red","aqua","yellow","blue","magenta"]
for i in range(20):
    for color in colours:
        turtle.color(color)
        turtle.circle(120)
        turtle.right(10)


turtle.mainloop()