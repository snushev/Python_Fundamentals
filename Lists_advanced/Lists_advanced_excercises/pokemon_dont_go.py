sequence = list(map(int, input().split()))
result = 0
while len(sequence) > 0:
    index = int(input())

    if index < 0:
        current_num = sequence[0]
        result += current_num
        sequence[0] = sequence[-1]

    elif index >= len(sequence):
        current_num = sequence[-1]
        result += current_num
        sequence[-1] = sequence[0]
    else:
        result += sequence[index]
        current_num = sequence[index]
        sequence.pop(index)

    sequence = [num + current_num if num <= current_num else num - current_num for num in sequence]
print(result)