number_of_strings = int(input())
word = input()
my_list = []
filtered_list = []

for _ in range(number_of_strings):
    new_string = input()
    my_list.append(new_string)
    if word in new_string:
        filtered_list.append(new_string)

print(my_list)
print(filtered_list)