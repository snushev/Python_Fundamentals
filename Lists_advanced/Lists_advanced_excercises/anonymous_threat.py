my_list = input().split()

while True:
    command = input()

    if command == "3:1":
        break

    command_parts = command.split()

    if command_parts[0] == "merge":
        start_index = int(command_parts[1])
        end_index = int(command_parts[2])

        start_index = max(0, start_index)
        end_index = min(len(my_list) - 1, end_index)

        if start_index <= end_index:
            merged_string = ''.join(my_list[start_index:end_index + 1])
            my_list = my_list[:start_index] + [merged_string] + my_list[end_index + 1:]

    elif command_parts[0] == "divide":
        index = int(command_parts[1])
        partitions = int(command_parts[2])

        if partitions > 0 and 0 <= index < len(my_list):
            item = my_list[index]

            part_length = len(item) // partitions
            remainder = len(item) % partitions

            divided_parts = []
            start = 0

            for i in range(partitions):
                extra = 1 if i < remainder else 0
                divided_parts.append(item[start:start + part_length + extra])
                start += part_length + extra

            my_list = my_list[:index] + divided_parts + my_list[index + 1:]

print(' '.join(my_list))
