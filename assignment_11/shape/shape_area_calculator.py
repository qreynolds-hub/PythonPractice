from rectangle import Rectangle
from circle import Circle


def main():
    shapes = [
        Rectangle(4, 5),
        Circle(3),
        Rectangle(4, 4),
        Circle(1.5)
    ]

    print("Areas of various shapes:")
    for shape in shapes:
        print(f"{shape.__class__.__name__} area: {shape.area():.2f}")


if __name__ == "__main__":
    main()
