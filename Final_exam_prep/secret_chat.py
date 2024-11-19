message = input()

while True:
    command = input()
    if command == 'Reveal':
        break

    parts = command.split(':|:')
    action = parts[0]

    if action == 'InsertSpace':
        index = int(parts[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif action == 'Reverse':
        substring = parts[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            substring = substring[::-1]
            message += substring
            print(message)
        else:
            print('error')
    elif action == "ChangeAll":
        substring = parts[1]
        new_substring = parts[2]
        if substring in message:
            message = message.replace(substring, new_substring)
        print(message)

print(f"You have a new text message: {message}")