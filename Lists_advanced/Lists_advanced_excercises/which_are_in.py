fist_sequence = input().split(', ')
second_sequence = input().split(', ')
sequence = []

for first_string in fist_sequence:
    for second_string in second_sequence:
        if first_string in second_string:
            sequence.append(first_string)
            break

print(sequence)