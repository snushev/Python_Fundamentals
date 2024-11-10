number = int(input())
wanted_number = int(input())
binary_num = []
counter = 0
while number > 0:

    if number % 2 == 0 and wanted_number == 0:
        binary_num.insert(0, 0)
        counter += 1
    elif number % 2 == 1 and wanted_number == 1:
        binary_num.insert(0, 1)
        counter += 1

    number = number // 2
print(counter)