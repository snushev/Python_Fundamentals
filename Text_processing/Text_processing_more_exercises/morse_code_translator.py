morse_code_dict = {
    ".-": 'A', "-...": 'B', "-.-.": 'C', "-..": 'D', ".": 'E',
    "..-.": 'F', "--.": 'G', "....": 'H', "..": 'I', ".---": 'J',
    "-.-": 'K', ".-..": 'L', "--": 'M', "-.": 'N', "---": 'O',
    ".--.": 'P', "--.-": 'Q', ".-.": 'R', "...": 'S', "-": 'T',
    "..-": 'U', "...-": 'V', ".--": 'W', "-..-": 'X', "-.--": 'Y',
    "--..": 'Z', "-----": '0', ".----": '1', "..---": '2', "...--": '3',
    "....-": '4', ".....": '5', "-....": '6', "--...": '7', "---..": '8',
    "----.": '9'
}

code = input().split(' | ')
decypher = ""
for word in code:
    current_word = word.split()
    for i in current_word:
        for k in morse_code_dict:
            decypher += morse_code_dict[k]
            break
    decypher += " "
print(decypher)




