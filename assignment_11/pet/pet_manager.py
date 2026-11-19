from dog import Dog
from cat import Cat
from bird import Bird


def display_menu():
    print("\nPet Menu")
    print(" 1. Add Dog")
    print(" 2. Add Cat")
    print(" 3. Add Bird")
    print(" 4. Show All Pets")
    print(" 5. Exit")


def main():
    pets = []

    while True:
        display_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter dog's name: ")
            pets.append(Dog(name))
        elif choice == "2":
            name = input("Enter cat's name: ")
            pets.append(Cat(name))
        elif choice == "3":
            name = input("Enter bird's name: ")
            pets.append(Bird(name))
        elif choice == "4":
            print("\nYour Pets:")
            for pet in pets:
                print(
                    f"{pet.name} the {pet.__class__.__name__} "
                    f"says {pet.speak()}"
                )
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
