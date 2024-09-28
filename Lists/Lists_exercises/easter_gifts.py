gifts = input().split()

while True:
    command = input()

    if command == "No Money":
        break

    command_parts = command.split()
    action = command_parts[0]

    if action == "OutOfStock":
        gift_to_replace = command_parts[1]
        for i in range(len(gifts)):
            if gifts[i] == gift_to_replace:
                gifts[i] = "None"

    elif action == "Required":
        gift = command_parts[1]
        index = int(command_parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif action == "JustInCase":
        gift = command_parts[1]
        gifts[-1] = gift


final_gifts = []
for gift in gifts:
    if gift != "None":
        final_gifts.append(gift)

print(" ".join(final_gifts))
