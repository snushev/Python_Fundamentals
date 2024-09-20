number = int(input())
is_true = True
for i in range(number - 1, 1, -1):
    if number % i == 0:
        is_true = False
        break
print(is_true)