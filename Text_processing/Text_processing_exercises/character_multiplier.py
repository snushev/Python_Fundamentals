first, second = input().split()
shorter_str = ""
longer_str = ''
total = 0
if len(first) < len(second):
    shorter_str = first
    longer_str = second
else:
    shorter_str = second
    longer_str = first

for i in range(len(shorter_str)):
    total += ord(shorter_str[i]) * ord(longer_str[i])

for i in range(len(shorter_str), len(longer_str)):
    total += ord(longer_str[i])

print(total)