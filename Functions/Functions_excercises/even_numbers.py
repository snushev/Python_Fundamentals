# Function to filter even numbers
def get_even_numbers(numbers: str) -> list:
    num_list = map(int, numbers.split())
    even_numbers = list(filter(lambda x: x % 2 == 0, num_list))

    return even_numbers



numbers = input()
even_numbers = get_even_numbers(numbers)
print(even_numbers)