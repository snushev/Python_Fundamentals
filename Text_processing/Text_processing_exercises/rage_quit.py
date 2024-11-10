text = input()
unique_symbols = set()
final_message = []

i = 0
while i < len(text):
    current_str = ""
    while i < len(text) and not text[i].isdigit():
        current_str += text[i].upper()
        unique_symbols.add(text[i].lower())
        i += 1

    num_str = ""
    while i < len(text) and text[i].isdigit():
        num_str += text[i]
        i += 1

    if num_str:
        times_to_print = int(num_str)
        final_message.append(current_str * times_to_print)

print(f"Unique symbols used: {len(unique_symbols)}")
print("".join(final_message))
