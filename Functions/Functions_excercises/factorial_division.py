def factorial(number: int) -> int:
    for i in range(1, number):
        number *= i
    return number


first_number = int(input())
second_number = int(input())
first_factorial = factorial(first_number)
second_factorial = factorial(second_number)
result = first_factorial / second_factorial
print(f'{result:.2f}')