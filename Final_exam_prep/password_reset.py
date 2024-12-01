text = input()

while True:
    command = input()

    if command == "Done":
        break

    parts = command.split(" ")
    action = parts[0]
    if action == "TakeOdd":
        new_text = ""
        for index, char in enumerate(text):
            if index % 2 != 0:
                new_text += char
        text = new_text
        print(text)
    elif action == "Cut":
        index = int(parts[1])
        length = int(parts[2])
        substring = text[index:index+length]
        text = text.replace(substring, "", 1)
        print(text)
    elif action == "Substitute":
        substring = parts[1]
        substitute = parts[2]
        if substring in text:
            text = text.replace(substring, substitute)
            print(text)
        else:
            print("Nothing to replace!")


print(f"Your password is: {text}")