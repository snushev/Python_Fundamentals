s = input()
result = []
delete_strength = 0

for i in range(len(s)):
    if s[i] == '>':
        result.append(s[i])
        delete_strength += int(s[i + 1])
    elif delete_strength > 0:
        delete_strength -= 1
    else:
        result.append(s[i])
    
print("".join(result))
