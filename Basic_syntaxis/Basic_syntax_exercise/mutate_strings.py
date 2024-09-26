first = input()
second = input()
last_printed = first
for char1 in range(len(first)):
    left_index = second[:char1 + 1]
    right_index = first[char1 + 1:]
    new_string = left_index + right_index
    if new_string != last_printed:
        print(new_string)
        last_printed = new_string
