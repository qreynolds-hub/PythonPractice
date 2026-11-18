
import turtle

# Set up the turtle window
turtle.setup(width=500, height=600)
turtle.hideturtle()
turtle.fillcolor("orange")
turtle.speed(3)

# Draw the first diamond
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.begin_fill()

for i in range(2):
    turtle.forward(80)
    turtle.right(60)
    turtle.forward(80)
    turtle.right(120)

turtle.end_fill()

# Draw the second diamond
turtle.penup()
turtle.goto(60, 0)
turtle.pendown()
turtle.begin_fill()

for i in range(2):
    turtle.forward(80)
    turtle.right(60)
    turtle.forward(80)
    turtle.right(120)

turtle.end_fill()

turtle.done()
