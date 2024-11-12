key = list(map(int, input().split()))
some_string = input()

while some_string != "find":
    new_string = ""
    for index, char in enumerate(some_string):
        current_key = index % len(key)
        char_value = ord(char) - key[current_key]
        new_char = chr(char_value)
        new_string += new_char
    treasure = new_string[new_string.index("&") + 1:new_string.index("&", new_string.index("&") + 1)]
    coordinates = new_string[new_string.index("<") + 1:new_string.index(">")]
    print(f"Found {treasure} at {coordinates}")
    some_string = input()
