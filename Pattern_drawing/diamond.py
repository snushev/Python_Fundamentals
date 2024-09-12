height = int(input())

mid = height // 2 + 1

for i in range(1, mid + 1):
    print(" " * (mid - i) + "*" * (2 * i - 1))
for i in range(mid - 1, 0, -1):
    print(" " * (mid - i) + "*" * (2 * i - 1))