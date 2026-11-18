
import turtle

SQUARE = "1"
CIRCLE = "2"
TRIANGLE = "3"
QUIT = "4"


def main():
    choice = ""

    while choice != QUIT:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == SQUARE:
            square(-100, 0, 100, "red")
        elif choice == CIRCLE:
            circle(100, 100, 100, "blue")
        elif choice == TRIANGLE:
            equilateral_triangle(-50, 0, 100, "green")
        elif choice == QUIT:
            print("Goodbye!")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

    turtle.done()


def display_menu():
    print()
    print("Shape Menu")
    print("1) Draw a Square")
    print("2) Draw a Circle")
    print("3) Draw an Equilateral Triangle")
    print("4) Quit")


# Draw a square starting at coordinate x, y
def square(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(side)
        turtle.left(90)

    turtle.end_fill()
    turtle.penup()


# Draw an equilateral triangle starting at coordinate x, y
def equilateral_triangle(x, y, side, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()

    for count in range(3):
        turtle.forward(side)
        turtle.left(120)

    turtle.end_fill()
    turtle.penup()


# Draw a circle using coordinate x, y as its center
def circle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()


if __name__ == "__main__":
    main()
