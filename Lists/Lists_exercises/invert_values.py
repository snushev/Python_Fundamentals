string_in_numbers = input()
values_list = string_in_numbers.split(" ")
int_list = []

for value in values_list:
    reverse_value = int(value)
    int_list.append(reverse_value * -1)

print(int_list)
