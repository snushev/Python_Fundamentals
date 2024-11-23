initial_tour = input()

while True:
    command = input()
    if command == "Travel":
        break

    parts = command.split(":")
    action = parts[0]
    if action == "Add Stop":
        index = int(parts[1])
        string_ = parts[2]
        if 0 <= index < len(initial_tour):
            initial_tour = initial_tour[:index] + string_ + initial_tour[index:]
        print(initial_tour)
    elif action == "Remove Stop":
        start_index = int(parts[1])
        end_index = int(parts[2])
        if 0 <= start_index <= end_index < len(initial_tour):
            initial_tour = initial_tour[:start_index] + initial_tour[end_index + 1:]
        print(initial_tour)
    elif action == "Switch":
        old_string = parts[1]
        new_string = parts[2]
        if old_string in initial_tour:
            initial_tour = initial_tour.replace(old_string, new_string)
        print(initial_tour)

print(f"Ready for world tour! Planned stops: {initial_tour}")
