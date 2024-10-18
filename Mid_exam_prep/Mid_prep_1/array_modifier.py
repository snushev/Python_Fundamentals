def swap(initial_list, current_command):
    index1 = int(current_command[1])
    index2 = int(current_command[2])
    initial_list[index1], initial_list[index2] = initial_list[index2], initial_list[index1]
    return initial_list


def multiply(initial_list, current_command):
    index1 = int(current_command[1])
    index2 = int(current_command[2])
    initial_list[index1] *= initial_list[index2]
    return initial_list


def decrease(initial_list):
    initial_list = [num - 1 for num in initial_list]
    return initial_list


initial_array = list(map(int, input().split()))
command = input().split()

while command[0] != "end":
    if command[0] == "swap":
        initial_array = swap(initial_array, command)
    elif command[0] == "multiply":
        initial_array = multiply(initial_array, command)
    elif command[0] == "decrease":
        initial_array = decrease(initial_array)

    command = input().split()

print(", ".join(list(map(str, initial_array))))