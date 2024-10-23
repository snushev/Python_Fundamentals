def add(cards_list, command):
    current_card = command[1]
    if current_card in cards_list:
        print("Card is already in the deck")
    else:
        cards_list.append(current_card)
        print("Card successfully added")
    return cards_list


def remove(cards_list, command):
    current_card = command[1]
    if current_card in cards_list:
        cards_list.remove(current_card)
        print("Card successfully removed")
    else:
        print("Card not found")
    return cards_list


def remove_at(cards_list, command):
    index = int(command[1])
    if index in range(len(cards_list)):
        cards_list.pop(index)
        print("Card successfully removed")
    else:
        print("Index out of range")
        return cards_list


def insert(cards_list, command):
    index, current_card = int(command[1]), command[2]
    if index not in range(len(cards_list)):
        print("Index out of range")
    elif current_card in cards_list:
        print("Card is already added")
    else:
        cards_list.insert(index, current_card)
        print("Card successfully added")
    return cards_list


def main():
    cards = input().split(", ")
    number_of_commands = int(input())

    for _ in range(number_of_commands):
        command = input().split(", ")
        current_command = command[0]

        if current_command == "Add":
            cards = add(cards, command)
        elif current_command == "Remove":
            cards = remove(cards, command)
        elif current_command == "Remove At":
            cards = remove_at(cards, command)
        elif current_command == "Insert":
            cards = insert(cards, command)

    print(", ".join(cards))


main()