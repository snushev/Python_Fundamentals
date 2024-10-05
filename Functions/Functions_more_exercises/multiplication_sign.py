def multiplication(first_num, second_num, third_num):
    negative_count = sum(num < 0 for num in (first_num, second_num, third_num))

    if 0 in (first_num, second_num, third_num):
        return "zero"
    elif negative_count % 2 == 0:
        return "positive"
    return "negative"


first_number = int(input())
second_number = int(input())
third_number = int(input())

print(multiplication(first_number, second_number, third_number))