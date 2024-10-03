def find_smallest_number(a: int, b: int, c: int):
    return min(a, b, c)


a = int(input())
b = int(input())
c = int(input())

smallest_number = find_smallest_number(a, b, c)
print(smallest_number)