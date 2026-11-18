
def main():
    password = input("Enter a password: ")

    valid = True

    if len(password) < 8:
        print("Invalid: Password must be at least 8 characters long.")
        valid = False

    if not any(char.isupper() for char in password):
        print("Invalid: Password must contain at least one uppercase letter.")
        valid = False

    if not any(char.islower() for char in password):
        print("Invalid: Password must contain at least one lowercase letter.")
        valid = False

    if not any(char.isdigit() for char in password):
        print("Invalid: Password must contain at least one digit.")
        valid = False

    if not password.isalnum():
        print("Invalid: Password can only contain letters and digits.")
        valid = False

    if valid:
        print("Password is valid!")


if __name__ == "__main__":
    main()
