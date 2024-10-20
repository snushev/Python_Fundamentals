list_of_coffees = input().split(' ')
number_of_commands = int(input())

for command in range(number_of_commands):
    current_command = input().split(' ')

    if current_command[0] == 'Include':
        coffee = current_command[1]
        list_of_coffees.append(coffee)
    elif current_command[0] == 'Remove':
        first_last = current_command[1]
        num_of_coffees = int(current_command[2])
        if num_of_coffees <= len(list_of_coffees):
            if first_last == "first":
                del list_of_coffees[:num_of_coffees]
            elif first_last == "last":
                del list_of_coffees[-num_of_coffees:]
    elif current_command[0] == "Prefer":
        coffee1 = int(current_command[1])
        coffee2 = int(current_command[2])
        if coffee1 in range(len(list_of_coffees)) and coffee2 in range(len(list_of_coffees)):
            list_of_coffees[coffee1], list_of_coffees[coffee2] = list_of_coffees[coffee2], list_of_coffees[coffee1]
    elif current_command[0] == "Reverse":
        list_of_coffees = list_of_coffees[::-1]
print(f"Coffees:\n\n{' '.join(list_of_coffees)}")