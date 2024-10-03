def sum_numbers(a, b):
    return a + b


def subtract(sum_result, c):
    return sum_result - c


def add_and_subtract(a, b, c):
    sum_result = sum_numbers(a, b)
    result = subtract(sum_result, c)
    print(result)


a = int(input())
b = int(input())
c = int(input())

add_and_subtract(a, b, c)