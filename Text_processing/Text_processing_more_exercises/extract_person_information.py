n = int(input())

for i in range(n):
    text = input()
    name = ""
    age = ""
    if "@" in text and "|" in text:
        start_index = text.index("@")
        end_index = text.index("|")
        name = text[start_index + 1:end_index]
    if "#" in text and "*" in text:
        start_index = text.index("#")
        end_index = text.index("*")
        age = text[start_index + 1:end_index]
    print(f"{name} is {age} years old.")