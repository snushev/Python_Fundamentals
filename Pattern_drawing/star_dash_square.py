n = int(input())

for row in range(1, n + 1):
    for col in range(1, n + 1):
        if (row + col) % 2 == 0:
            print("*", end='')
        else:
            print("-", end='')
    print()
