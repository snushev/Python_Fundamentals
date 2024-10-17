def fire(ship_sections, current_command):
    index, damage = int(current_command[1]), int(current_command[2])
    if index in range(len(ship_sections)):
        ship_sections[index] -= damage
        if ship_sections[index] <= 0:
            return ship_sections, True
    return ship_sections, False


def defend():
    pass


def repair(s):
    pass


def status():
    pass


pirate_ship_sections = list(map(int, input().split('>')))
warship_sections = list(map(int, input().split('>')))
max_health_per_section = int(input())
pirate_ship_has_sunken = False
warship_has_sunken = False

command = input().split(' ')
while command[0] != "Retire":
    action = command[0]
    if action == "Fire":
        warship_sections, warship_has_sunken = fire(warship_sections, action)
    elif action == "Defend":
        pass
    elif action == "Repair":
        pass
    elif action == "Status":
        pass


    command = input().split(' ')