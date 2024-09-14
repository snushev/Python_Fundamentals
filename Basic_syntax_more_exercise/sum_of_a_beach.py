word = input().lower()
words = ["water", "sand", "fish", "sun"]
counter = 0

for target in words:
    if target in word:
        counter += 1
print(counter)