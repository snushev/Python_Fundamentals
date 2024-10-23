def plant(crops, command):
    crop = command[1]
    if crop not in crops:
        crops.insert(0, crop)
    return crops


def transplant(crops, command):
    crop = command[1]
    if crop in crops:
        crops.append(crop)
        crops.remove(crop)
    return crops


def replace(crops, command):
    index_1 = int(command[1])
    index_2 = int(command[2])
    if 0 < index_1 < len(crops) and 0 < index_2 < len(crops):
        crops[index_1], crops[index_2] = crops[index_2], crops[index_1]
    return crops


def uproot(crops, command):
    crop = command[1]
    if crop in crops:
        crops.remove(crop)
    return crops


def main():
    crops = input().split(" & ")
    command = input()

    while command != "Collect!":
        command_parts = command.split()
        if command_parts[0] == "Plant":
            crops = plant(crops, command_parts)
        elif command_parts[0] == "Transplant":
            crops = transplant(crops, command_parts)
        elif command_parts[0] == "Replace":
            crops = replace(crops, command_parts)
        elif command_parts[0] == "Uproot":
            crops = uproot(crops, command_parts)

        command = input()

    print(" | ".join(crops))


main()
