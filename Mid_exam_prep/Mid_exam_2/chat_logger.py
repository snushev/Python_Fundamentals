def chat(command, log):
    message = command[1]
    log.append(message)
    return log


def delete(command, log):
    message = command[1]
    if message in log:
        log.remove(message)
    return log


def edit(command, log):
    message = command[1]
    new_message = command[2]
    if message in log:
        index = log.index(message)
        log[index] = new_message
    return log


def pin(command, log):
    message = command[1]
    if message in log:
        log.append(message)
        log.remove(message)
    return log


def spam(command, log):
    [log.append(item) for item in command[1:]]
    return log


def main():
    command = input()
    chat_log = []
    while command != "end":
        command = command.split()
        if command[0] == "Chat":
            chat_log = chat(command, chat_log)
        elif command[0] == "Delete":
            chat_log = delete(command, chat_log)
        elif command[0] == "Edit":
            chat_log = edit(command, chat_log)
        elif command[0] == "Pin":
            chat_log = pin(command, chat_log)
        elif command[0] == "Spam":
            chat_log = spam(command, chat_log)

        command = input()
    print('\n'.join(chat_log))

main()