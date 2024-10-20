def add(numbers, command):
    value = int(command[1])
    numbers.append(value)
    return numbers


def remove(numbers, command):
    value = int(command[1])
    if value in numbers:
        numbers.remove(value)
    return numbers


def replace(numbers, command):
    value = int(command[1])
    replacement = int(command[2])
    if value in numbers:
        index = numbers.index(value)
        numbers[index] = replacement
    return numbers


def collapse(numbers, command):
    value = int(command[1])
    numbers = [x for x in numbers if x >= value]
    return numbers


def main():
    numbers = list(map(int, input().split()))
    command = input().split()

    while command[0] != 'Finish':
        if command[0] == 'Add':
            numbers = add(numbers, command)
        elif command[0] == 'Remove':
            numbers = remove(numbers, command)
        elif command[0] == 'Replace':
            numbers = replace(numbers, command)
        elif command[0] == "Collapse":
            numbers = collapse(numbers, command)

        command = input().split()
    print(" ".join(map(str, numbers)))

main()