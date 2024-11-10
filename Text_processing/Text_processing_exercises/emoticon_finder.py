text = input()

for index, char in enumerate(text):
    if char == ':':
        print(f':{text[index + 1]}')