text = input()

while True:
    command = input()

    if command == "Generate":
        break

    parts = command.split('>>>')
    action = parts[0]
    if action == "Contains":
        substring = parts[1]
        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")
    elif action == "Flip":
        case = parts[1]
        start_index = int(parts[2])
        end_index = int(parts[3])
        part = text[start_index:end_index]
        if case == "Upper":
            part = part.upper()
        elif case == "Lower":
            part = part.lower()
        text = text[:start_index] + part + text[end_index:]
        print(f"{text}")
    elif action == "Slice":
        start_index = int(parts[1])
        end_index = int(parts[2])
        text = text[:start_index] + text[end_index:]
        print(text)

print(f"Your activation key is: {text}")