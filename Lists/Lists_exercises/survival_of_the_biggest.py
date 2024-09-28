import sys

numbers_list = input().split(' ')
count_of_numbers_to_remove = int(input())

for count in range(count_of_numbers_to_remove):
    smallest_number = sys.maxsize
    for current in numbers_list:
        if int(current) < smallest_number:
            smallest_number = int(current)
    numbers_list.remove(str(smallest_number))

print(', '.join(numbers_list))
