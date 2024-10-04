def get_even_numbers(numbers: str) -> list:
    num_list = map(int, numbers.split())
    even_numbers = list(filter(lambda x: x % 2 == 0, num_list))

    return even_numbers



nums = input()
even_numbers = get_even_numbers(nums)
print(even_numbers)
