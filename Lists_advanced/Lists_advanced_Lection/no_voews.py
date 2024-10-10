text = input()
vowels = ['a', 'e', 'o', 'i', 'u']
edited_text = [char for char in text if char.lower() not in vowels]

print("".join(edited_text))