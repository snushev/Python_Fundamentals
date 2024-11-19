username = input()

while True:
    command = input()
    if command == "Registration":
        break

    parts = command.split()
    action = parts[0]
    if action == "Letters":
        lower_upper = parts[1]
        if lower_upper == "Lower":
            username = username.lower()
        elif lower_upper == "Upper":
            username = username.upper()
        print(username)
    elif action == "Reverse":
        start_index = int(parts[1])
        end_index = int(parts[2])
        if 0 <= start_index <= end_index <= len(username):
            substring = username[start_index:end_index+1]
            reversed_substring = substring[::-1]
            print(reversed_substring)
    elif action == "Substring":
        substring = parts[1]
        if substring in username:
            username = username.replace(substring, "")
            print(username)
        else:
            print(f"The username {username} doesn't contain {substring}.")
    elif action == "Replace":
        char = parts[1]
        username = username.replace(char, "-")
        print(username)
    elif action == "IsValid":
        char = parts[1]
        if char in username:
            print("Valid username.")
        else:
            print(f"{char} must be contained in your username.")
