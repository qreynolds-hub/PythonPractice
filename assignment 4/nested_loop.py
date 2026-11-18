
# Print a decreasing triangle pattern

for row in range(7, 0, -1):
    for column in range(row):
        print("*", end=" ")
    print()
