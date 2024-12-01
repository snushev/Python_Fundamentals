text = input()

while True:
    command = input()

    if command == "Finalize":
        break
    elif command == "Encrypt":
        text = text[::-1]
        print(text)
        continue
    elif command == "Decrypt":
        text = text.swapcase()
        print(text)
        continue

    parts = command.split()
    action = parts[0]

    if action == "Substitute":
        old_char = parts[1]
        new_char = parts[2]
        if old_char in text:
            text = text.replace(old_char, new_char)
            print(text)
        else:
            print(f"Character not found.")
    elif action == "Scramble":
        index = int(parts[1])
        char = parts[2]
        if 0 <= index < len(text):
            text = text[:index] + char + text[index + 1:]
            print(text)
        else:
            print(f"Index out of bounds.")
    elif action == "Remove":
        substring = parts[1]
        text = text.replace(substring, "")
        print(text)
    else:
        print("Invalid command detected!")