numbers = list(map(int, input().split(', ')))
even_numbers = [index for index, num in enumerate(numbers) if num % 2 == 0]
print(even_numbers)

