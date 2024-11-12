first_char = ord(input())
second_char = ord(input())
text = input()

lower_char = min(first_char, second_char)
higher_char = max(first_char, second_char)

sum_of_chars = sum(ord(x) for x in text if lower_char < ord(x) < higher_char)

print(sum_of_chars)