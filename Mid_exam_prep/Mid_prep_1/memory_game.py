elements = input().split()
number_of_moves = 0

while elements:

    command = input().split()
    if command[0] == "end":
        print("Sorry you lose :(")
        print(' '.join(elements))
        break

    first_index, second_index = int(command[0]), int(command[1])
    number_of_moves += 1
    if first_index not in range(len(elements)) or second_index not in range(len(elements)):
        print("Invalid input! Adding additional elements to the board")
        mid_of_elements = len(elements) // 2
        elements.insert(mid_of_elements, "-" + str(number_of_moves) + "a")
        elements.insert(mid_of_elements, "-" + str(number_of_moves) + "a")
    elif elements[first_index] == elements[second_index]:
        print(f"Congrats! You have found matching elements - {elements[first_index]}!")
        elements.pop(max(first_index, second_index))
        elements.pop(min(first_index, second_index))

    else:
        print("Try again!")


else:
    print(f"You have won in {number_of_moves} turns!")
