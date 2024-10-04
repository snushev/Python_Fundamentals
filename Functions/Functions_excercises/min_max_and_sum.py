def min_max_sum(numbers):
    return min(numbers), max(numbers), sum(numbers)


numbers = list(map(int, input().split()))
min_number, max_number, sum_number = min_max_sum(numbers)
print(f'The minimum number is {min_number}')
print(f'The maximum number is {max_number}')
print(f'The sum number is: {sum_number}')
