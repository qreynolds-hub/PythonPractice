# This program converts Celsius temperatures to Fahrenheit
# from 0 up to the temperature entered by the user.

# Define the constant for absolute zero in Celsius
ABSOLUTE_ZERO = -273.15

# Input - Get a valid Celsius temperature from the user
while True:
    try:
        celsius = int(input("Enter a Celsius temperature: "))

        # Validate the temperature
        if celsius < ABSOLUTE_ZERO:
            print("Error: Temperature cannot be below absolute zero.")
            print("Please enter a valid temperature.")
        else:
            break

    except ValueError:
        print("Error: Please enter a whole number.")

# Process and Output - Convert Celsius to Fahrenheit
print(f"{'Celsius':<12}{'Fahrenheit':<12}")
print("-" * 24)

# Loop from 0 to the user's Celsius temperature
for degree in range(0, celsius + 1):
    fahrenheit = (degree * 9 / 5) + 32

    # Display the results in two columns
    print(f"{degree:<12}{fahrenheit:<12.2f}")
