
from pathlib import Path

MIN_CELSIUS = 0
MAX_CELSIUS = 50

# Find the file in the same folder that hosts the Python script
TEMPERATURE_FILE = Path(__file__).resolve().parent / "temperature_forloop.txt"


def main():
    celsius = get_celsius()

    # Test both for-loop and while-loop searches
    fahrenheit_forloop = find_match_forloop(celsius)
    fahrenheit_whileloop = find_match_whileloop(celsius)

    print(f"For-loop search result:   {fahrenheit_forloop}")
    print(f"While-loop search result: {fahrenheit_whileloop}")

    if fahrenheit_forloop is not None:
        print(
            f"Match found: {celsius} Celsius is "
            f"{fahrenheit_forloop:.2f} Fahrenheit."
        )
    else:
        fahrenheit = (celsius * 1.8) + 32
        append_record(celsius, fahrenheit)
        print(
            f"No match found. New record added: {celsius} Celsius = "
            f"{fahrenheit:.2f} Fahrenheit."
        )


def get_celsius():
    # Validate that the user enters a whole number between 0 and 50
    while True:
        try:
            celsius = int(input("Enter Celsius temperature (0-50): "))

            if MIN_CELSIUS <= celsius <= MAX_CELSIUS:
                return celsius
            else:
                print("Invalid input. Enter a value between 0 and 50.")

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def find_match_forloop(celsius):
    fahrenheit = None

    with open(TEMPERATURE_FILE, "r") as infile:
        skip_header(infile)

        for line in infile:
            # Split each record into two variables
            degree_text, fahrenheit_text = line.split("\t\t")

            if int(degree_text) == celsius:
                fahrenheit = float(fahrenheit_text)
                break

    return fahrenheit


def find_match_whileloop(celsius):
    fahrenheit = None

    with open(TEMPERATURE_FILE, "r") as infile:
        skip_header(infile)

        line = infile.readline()

        while line:
            # Split each record into two variables
            degree_text, fahrenheit_text = line.split("\t\t")

            if int(degree_text) == celsius:
                fahrenheit = float(fahrenheit_text)
                break

            line = infile.readline()

    return fahrenheit


# Remove the header and dashed separator line
def skip_header(infile):
    infile.readline()
    infile.readline()


def append_record(celsius, fahrenheit):
    # Append a new record without overwriting existing records
    with open(TEMPERATURE_FILE, "a") as outfile:
        outfile.write(f"{celsius:>8}\t\t{fahrenheit:>8.2f}\n")


if __name__ == "__main__":
    main()
