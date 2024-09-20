number_of_symbols = int(input())

for i in range(number_of_symbols):
    for j in range(number_of_symbols):
        for k in range(number_of_symbols):
            print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")