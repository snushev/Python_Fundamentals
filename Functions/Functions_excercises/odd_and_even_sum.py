def even_and_odd(number):
    odd_sum = 0
    even_sum = 0
    for i in number:
        if int(i) % 2 == 0:
            even_sum += int(i)
        else:
            odd_sum += int(i)
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

number = input()
print(even_and_odd(number))