# This program converts a temperature from Fahrenheit to Celsius.
# prompt the user to enter a temperature in Fahrenheit, 

fahrenheit = float(input("Enter the Fahrenheit temperature: "))

# generate the Celsius temperature using the formula: C = (F - 32) * 5/9
celsius = (fahrenheit - 32) * 5 / 9

# display the Celsius temperature to the user
print(f"The Celsius temperature is {celsius:.2f}")
