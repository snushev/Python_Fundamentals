def chars_in_range(start: str, end: str):
    all_chars = []
    for i in range(ord(start) + 1, ord(end)):
        all_chars.append(chr(i))
    return all_chars


start = input()
end = input()

chars = chars_in_range(start, end)
print(" ".join(chars))