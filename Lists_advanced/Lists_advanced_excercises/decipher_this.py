def decipher(code):
    deciphered_code = []
    for word in code_for_decipher:
        character = [char for char in word if char.isdigit()]
        letters = [char for char in word if char.isalpha()]
        letters[0], letters[-1] = letters[-1], letters[0]
        x = "".join(character)
        y = "".join(letters)
        new_word = "".join(chr(int(x)) + y)
        deciphered_code.append(new_word)
    return deciphered_code


code_for_decipher = input().split()
code = decipher(code_for_decipher)
print(' '.join(code))