def tribonacci(num):
    if num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    elif num == 3:
        return [1, 1, 2]

    tribonacci_sequence = [1, 1, 2]

    for i in range(3, num):
        next_value = tribonacci_sequence[i - 1] + tribonacci_sequence[i - 2] + tribonacci_sequence[i - 3]
        tribonacci_sequence.append(next_value)

    return tribonacci_sequence


number = int(input())
sequence = tribonacci(number)
print(" ".join(map(str,sequence)))
