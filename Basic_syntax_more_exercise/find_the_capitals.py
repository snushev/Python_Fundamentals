word = input()
capital_positions = []

for index, char in enumerate(word):
    if char.isupper():
        capital_positions.append(index)

print(capital_positions)
