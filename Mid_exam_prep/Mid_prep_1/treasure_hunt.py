def loot(initial_chest, command_):
    for item in command[1:]:
        if item not in initial_chest:
            initial_chest.insert(0, item)
    return initial_chest


def drop(initial_chest, command_):
    index = int(command[1])
    if 0 <= index < len(initial_chest):
        initial_chest.append(initial_chest[index])
        initial_chest.pop(index)
    return initial_chest


def steal(initial_chest, command_):
    count = int(command[1])
    stolen_items = []
    if count > len(initial_chest):
        count = len(initial_chest)
    stolen_items = initial_chest[-count:]
    initial_chest = initial_chest[:-count]
    return stolen_items, initial_chest


initial_treasure_chest = input().split('|')
command = input().split(' ')

while True:
    if command[0] == "Yohoho!":
        break
    elif command[0] == "Loot":
        initial_treasure_chest = loot(initial_treasure_chest, command)
    elif command[0] == "Drop":
        initial_treasure_chest = drop(initial_treasure_chest, command)
    elif command[0] == "Steal":
        stolen_items, initial_treasure_chest = steal(initial_treasure_chest, command)
        print(", ".join(stolen_items))

    command = input().split(' ')


if not initial_treasure_chest:
    print("Failed treasure hunt.")
else:
    treasure_points = [len(item) for item in initial_treasure_chest]
    treasure_points_ = sum(treasure_points)
    print(f"Average treasure gain: {treasure_points_ / len(initial_treasure_chest):.2f} pirate credits.")
