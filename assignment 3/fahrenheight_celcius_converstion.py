# This program converts temperatures between Fahrenheit and Celsius.
# It also checks that temperatures are not below absolute zero.

# define constants
ABSOLUTE_ZERO_F = -459.67
ABSOLUTE_ZERO_C = -273.15

# prompt the user to choose a temperature conversion
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")

choice = input("Enter 1 or 2: ")

# convert Fahrenheit to Celsius
if choice == "1":
    fahrenheit = float(input("Enter the Fahrenheit temperature: "))

    # check if temperature is valid
    while fahrenheit < ABSOLUTE_ZERO_F:
        print("Invalid temperature. Below absolute zero.")
        print("Please try again.")
        fahrenheit = float(input("Enter the Fahrenheit temperature: "))

    # generate Celsius using C = (F - 32) * 5/9
    celsius = (fahrenheit - 32) * 5 / 9

    # display the Celsius temperature
    print(f"The Celsius temperature is {celsius:.2f}")

# convert Celsius to Fahrenheit
elif choice == "2":
    celsius = float(input("Enter the Celsius temperature: "))

    # check if temperature is valid
    while celsius < ABSOLUTE_ZERO_C:
        print("Invalid temperature. Below absolute zero.")
        print("Please try again.")
        celsius = float(input("Enter the Celsius temperature: "))

    # generate Fahrenheit using F = (C * 9/5) + 32
    fahrenheit = (celsius * 9 / 5) + 32

    # display the Fahrenheit temperature
    print(f"The Fahrenheit temperature is {fahrenheit:.2f}")

else:
    print("Invalid choice. Please enter 1 or 2.")