height = int(input())

mid = height // 2 + 1

for i in range(1, mid + 1):
    for j in range(height - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print(j + 1, end="")
    print()
for i in range(mid - 1, 0, -1):
    for j in range(height - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print(j + 1, end="")
    print()