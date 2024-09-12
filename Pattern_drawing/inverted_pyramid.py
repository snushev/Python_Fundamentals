height = int(input())

for row in range(height, 0, -1):
    for col in range(height - row):
        print(" ", end="")
    for col in range(2 * row - 1):
        print("*", end="")
    print()