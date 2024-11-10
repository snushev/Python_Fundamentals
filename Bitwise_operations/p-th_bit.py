number = int(input())
bit = int(input())
binary_num = []
while number > 0:

    if number % 2 == 0:
        binary_num.insert(0, 0)

    else:
        binary_num.insert(0, 1)

    number = number // 2
print(f"{binary_num[-bit - 1]}")