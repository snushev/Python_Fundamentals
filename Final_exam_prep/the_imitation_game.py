def move(message_, number):
    message_1, message_2 = message_[:number], message_[number:]
    message_ = message_2 + message_1
    return message_


def insert(message_, index_, letter_):
    message_ = message_[:index_] + letter_ + message_[index_:]
    return message_


def replace(message_, substring_, replacement_):
    message_ = message_.replace(substring_, replacement_)
    return message_


message = input()

while True:
    command = input()

    if command == "Decode":
        break

    parts = command.split("|")
    action = parts[0]
    if action == "Move":
        number_of_letters = int(parts[1])
        message = move(message, number_of_letters)
    elif action == "Insert":
        index = int(parts[1])
        letter = parts[2]
        message = insert(message, index, letter)
    elif action == "ChangeAll":
        substring = parts[1]
        replacement = parts[2]
        message = replace(message, substring, replacement)

print(f"The decrypted message is: {message}")
