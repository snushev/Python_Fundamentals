def register(dict_, command_):
    if username not in dict_:
        dict_[username] = license_plate_number
        print(f"{username} registered {license_plate_number} successfully")
    else:
        print(f"ERROR: already registered with plate number {license_plate_number}")
    return dict_


def unregister(dict_, command_):
    if username in dict_:
        del dict_[username]
        print(f"{username} unregistered successfully")
    else:
        print(f"ERROR: user {username} not found")
    return dict_


number_of_commands = int(input())
db = {}

for i in range(number_of_commands):
    command = input().split()
    if command[0] == 'register':
        username = command[1]
        license_plate_number = command[2]
        db = register(db, command)
    elif command[0] == 'unregister':
        username = command[1]
        db = unregister(db, command)

for user in db:
    print(f"{user} => {db[user]}")

