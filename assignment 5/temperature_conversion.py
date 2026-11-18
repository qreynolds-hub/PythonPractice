
# Define Global Constants
CELSIUS = "C"
FAHRENHEIT = "F"


def main():
    temperature_type = get_temperature_type()
    temperature = get_temperature(temperature_type)
    display_conversion(temperature_type, temperature)


# Keep asking until a valid temperature type is received
def get_temperature_type():
    temperature_type = ""

    while temperature_type not in (CELSIUS, FAHRENHEIT):
        temperature_type = input(
            "Enter temperature type (C or F): "
        ).strip().upper()

        if temperature_type not in (CELSIUS, FAHRENHEIT):
            print("Invalid input! Enter C or F.")

    return temperature_type


# Keep asking until a valid number is received
def get_temperature(temperature_type):
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
            return temperature
        except ValueError:
            print("Invalid input! Enter a valid number.")


# Convert and display the temperature
def display_conversion(temperature_type, temperature):
    if temperature_type == CELSIUS:
        converted = (temperature * 9 / 5) + 32
        print(f"{temperature:.2f} Celsius = {converted:.2f} Fahrenheit")
    else:
        converted = (temperature - 32) * 5 / 9
        print(f"{temperature:.2f} Fahrenheit = {converted:.2f} Celsius")


if __name__ == "__main__":
    main()
