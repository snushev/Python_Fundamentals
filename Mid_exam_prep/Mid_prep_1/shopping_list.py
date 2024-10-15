initial_list = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break

    command_parts = command.split()

    if command_parts[0] == "Urgent":
        item = command_parts[1]
        if item not in initial_list:
            initial_list.insert(0, item)
    elif command_parts[0] == "Unnecessary":
        item = command_parts[1]
        if item in initial_list:
            initial_list.remove(item)
    elif command_parts[0] == "Correct":
        old_item = command_parts[1]
        new_item = command_parts[2]
        if old_item in initial_list:
            index = initial_list.index(old_item)
            initial_list[index] = new_item
    elif command_parts[0] == "Rearrange":
        item = command_parts[1]
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

print(", ".join(initial_list))
