text = input().split(" | ")
dict_ = {}
for pair in text:
    key, value = pair.split(":")
    if key not in dict_.keys():
        dict_[key] = []
    dict_[key].append(value.strip())

words = input().split(" | ")
command = input()

if command == "Test":
    for word in words:
        if word in dict_.keys():
            print(f"{word}:")
            for value in dict_[word]:
                print(f"-{value}")
elif command == "Hand Over":
    words = [x for x in dict_.keys()]
    print(" ".join(words))


