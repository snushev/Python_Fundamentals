num_of_messages = int(input())
message = ""
for i in range(num_of_messages):
    command = int(input())
    if command == 86:
        message = "How are you?"
    elif command == 88:
        message = "Hello"
    elif command < 88:
        message = "GREAT!"
    else:
        message = "Bye."
    print(message)
