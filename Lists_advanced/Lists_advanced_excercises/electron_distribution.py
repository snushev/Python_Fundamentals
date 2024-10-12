numbers = list(map(int, input().split(", ")))
current_group = 10
while numbers:
    filtered_numbers_for_current_group = [num for num in numbers if num <= current_group]
    numbers = [num for num in numbers if num > current_group]
    print(f'Group of {current_group}\'s: {filtered_numbers_for_current_group}')
    current_group += 10