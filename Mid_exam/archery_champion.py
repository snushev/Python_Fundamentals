def shoot_left(target_list, current_command, points):
    if 0 <= start_index < len(target_list):
        current_index = (start_index - length) % len(targets)
        target_list[current_index] -= 5
        if target_list[current_index] < 0:
            points += 5 + target_list[current_index]
            target_list[current_index] = 0
        else:
            points += 5
    return target_list, points


def shoot_right(target_list, current_command, points):
    if 0 <= start_index < len(target_list):
        current_index = (start_index + length) % len(targets)
        target_list[current_index] -= 5
        if target_list[current_index] < 0:
            points += 5 + target_list[current_index]
            target_list[current_index] = 0
        else:
            points += 5
    return target_list, points


def reverse_(target_list):
    target_list = target_list[::-1]
    return target_list


targets = list(map(int, input().split('|')))
total_points = 0

while True:
    command = input()

    if command == "Game over":
        break
    elif command == "Reverse":
        targets = reverse_(targets)
    else:
        command_parts = command.split('@')
        action = command_parts[0]
        start_index = int(command_parts[1])
        length = int(command_parts[2])

        if action == "Shoot Left":
            targets, total_points = shoot_left(targets, action, total_points)
        elif action == "Shoot Right":
            targets, total_points = shoot_right(targets, action, total_points)


print(' - '.join(list(map(str, targets))))
print(f'John finished the archery tournament with {total_points} points!')