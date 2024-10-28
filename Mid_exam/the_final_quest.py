message = input().split()
command = input()

while command != "Stop":
    if command == "Sort":
        message.sort(reverse=True)

    command_parts = command.split()
    action = command_parts[0]

    if action == "Delete":
        index = int(command_parts[1])
        if 0 <= index + 1 < len(message):
            message.pop(index + 1)
    elif action == "Swap":
        word1 = command_parts[1]
        word2 = command_parts[2]
        if word1 in message and word2 in message:
            index1 = message.index(word1)
            index2 = message.index(word2)
            message[index1], message[index2] = message[index2], message[index1]
    elif action == "Put":
        word = command_parts[1]
        index = int(command_parts[2])
        if 0 <= index - 1 <= len(message):
            if index == len(message):
                message.append(word)
            else:
                message.insert(index - 1, word)
    elif action == "Replace":
        word1 = command_parts[1]
        word2 = command_parts[2]
        if word2 in message:
            index = message.index(word2)
            message[index] = word1

    command = input()

print(" ".join(message))