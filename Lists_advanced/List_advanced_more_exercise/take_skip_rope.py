some_string = input()

digits = [int(num) for num in some_string if num.isdigit()]
take_list = [num for index, num in enumerate(digits) if index % 2 == 0]
skip_list = [num for index, num in enumerate(digits) if index % 2 != 0]
string_list = [char for char in some_string if not char.isdigit()]

result = []
for i in range(len(take_list)):
    result.append(''.join(string_list[:take_list[i]]))
    del string_list[:take_list[i]]
    del string_list[:skip_list[i]]

print("".join(result))


