number = int(input())

for i in range(number, 0, -1):
    for j in range(0, i):
        print('*', end='')
    print()