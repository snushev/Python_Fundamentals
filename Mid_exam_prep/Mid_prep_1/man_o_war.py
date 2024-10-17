def fire(ship_sections, current_command):
    index, damage = int(current_command[1]), int(current_command[2])
    if index in range(len(ship_sections)):
        ship_sections[index] -= damage
        if ship_sections[index] <= 0:
            return ship_sections, True
    return ship_sections, False


def defend(ship_sections, current_command):
    start_index, end_index, damage = int(current_command[1]), int(current_command[2]), int(current_command[3])
    if start_index in range(len(ship_sections)) and end_index in range(len(ship_sections)):
        for index in range(start_index, end_index + 1):
            ship_sections[index] -= damage
            if ship_sections[index] <= 0:
                return ship_sections, True
    return ship_sections, False


def repair(ship_sections, current_command):
    index, heal = int(current_command[1]), int(current_command[2])
    if index in range(len(ship_sections)):
        ship_sections[index] += heal
        if ship_sections[index] > max_health_per_section:
            ship_sections[index] = max_health_per_section
    return ship_sections


def status(ship_sections):
    count = 0
    for section in ship_sections:
        if section < max_health_per_section * 0.2:
            count += 1
    return count


pirate_ship_sections = list(map(int, input().split('>')))
warship_sections = list(map(int, input().split('>')))
max_health_per_section = int(input())
pirate_ship_has_sunken = False
warship_has_sunken = False

command = input().split(' ')
while command[0] != "Retire":
    action = command[0]
    if action == "Fire":
        warship_sections, warship_has_sunken = fire(warship_sections, command)
        if warship_has_sunken:
            print("You won! The enemy ship has sunken.")
            break
    elif action == "Defend":
        pirate_ship_sections, pirate_ship_has_sunken = defend(pirate_ship_sections, command)
        if pirate_ship_has_sunken:
            print(f"You lost! The pirate ship has sunken.")
            break

    elif action == "Repair":
        pirate_ship_sections = repair(pirate_ship_sections, command)
    elif action == "Status":
        sections_for_repair = status(pirate_ship_sections)
        print(f'{sections_for_repair} sections need repair.')
    command = input().split(' ')


else:
    print(f"Pirate ship status: {sum(pirate_ship_sections)}")
    print(f"Warship status: {sum(warship_sections)}")


