# Read the initial list from input
initial_list = list(map(int, input().split()))
command = input().split()

while True:
    if command[0] == "end":
        break

    elif command[0] == "exchange":
        index = int(command[1])
        if index < 0 or index >= len(initial_list):
            print("Invalid index")
        else:
            # Split and exchange
            initial_list = initial_list[index + 1:] + initial_list[:index + 1]

    elif command[0] == "max":
        if command[1] == "even":
            even_indices = [i for i, num in enumerate(initial_list) if num % 2 == 0]
            if even_indices:
                max_even_index = max(even_indices, key=lambda i: initial_list[i])
                print(max_even_index)
            else:
                print("No matches")
        elif command[1] == "odd":
            odd_indices = [i for i, num in enumerate(initial_list) if num % 2 != 0]
            if odd_indices:
                max_odd_index = max(odd_indices, key=lambda i: initial_list[i])
                print(max_odd_index)
            else:
                print("No matches")

    elif command[0] == "min":
        if command[1] == "even":
            even_indices = [i for i, num in enumerate(initial_list) if num % 2 == 0]
            if even_indices:
                min_even_index = min(even_indices, key=lambda i: (initial_list[i], -i))
                print(min_even_index)
            else:
                print("No matches")
        elif command[1] == "odd":
            odd_indices = [i for i, num in enumerate(initial_list) if num % 2 != 0]
            if odd_indices:
                min_odd_index = min(odd_indices, key=lambda i: (initial_list[i], -i))
                print(min_odd_index)
            else:
                print("No matches")

    elif command[0] == "first":
        count = int(command[1])
        if count < 0 or count > len(initial_list):
            print("Invalid count")
        elif command[2] == "even":
            first_even = [num for num in initial_list if num % 2 == 0][:count]
            print(first_even)
        elif command[2] == "odd":
            first_odd = [num for num in initial_list if num % 2 != 0][:count]
            print(first_odd)

    elif command[0] == "last":
        count = int(command[1])
        if count < 0 or count > len(initial_list):
            print("Invalid count")
        elif command[2] == "even":
            last_even = [num for num in initial_list if num % 2 == 0]
            print(last_even[-count:] if len(last_even) >= count else last_even)
        elif command[2] == "odd":
            last_odd = [num for num in initial_list if num % 2 != 0]
            print(last_odd[-count:] if len(last_odd) >= count else last_odd)

    command = input().split()

# Print the final state of the list
print(f"[{', '.join(map(str, initial_list))}]")
