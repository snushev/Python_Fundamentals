number = int(input())
words = {}

for num in range(number):
    key = input()
    value = input()
    if key in words:
        words[key] += ", " + value
    else:
        words[key] = value

for word in words:
    print(f"{word} - {words[word]}")