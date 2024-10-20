def blacklist(friends_list, command):
    name = command[1]
    if name in friends_list:
        print(f"{name} was blacklisted.")
        index = friends_list.index(name)
        friends_list[index] = "Blacklisted"
    else:
        print(f"{name} was not found.")
    return friends_list


def error(friends_list, command):
    index = int(command[1])
    if index in range(len(friends_list)):
        if friends_list[index] != "Blacklisted" and friends_list[index] != "Lost":
            print(f"{friends_list[index]} was lost due to an error.")
            friends_list[index] = "Lost"
    return friends_list


def change(friends_list, command):
    index = int(command[1])
    new_name = command[2]
    if index in range(len(friends_list)):
        print(f"{friends_list[index]} changed his username to {new_name}.")
        friends_list[index] = new_name
    return friends_list

def main():
    friends_list = input().split(', ')
    command = input().split()

    while command[0] != "Report":
        if command[0] == "Blacklist":
            friends_list = blacklist(friends_list, command)
        elif command[0] == "Error":
            friends_list = error(friends_list, command)
        elif command[0] == "Change":
            friends_list = change(friends_list, command)

        command = input().split()

    blacklisted = len([x for x in friends_list if x == "Blacklisted"])
    lost = len([x for x in friends_list if x == "Lost"])

    print(f"Blacklisted names: {blacklisted}")
    print(f"Lost names: {lost}")
    print(" ".join(friends_list))

main()