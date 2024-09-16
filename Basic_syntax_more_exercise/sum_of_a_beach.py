words = ["water", "sand", "fish", "sun"]
word = input().lower()
counter = 0

for target in words:
    counter += word.count(target)

print(counter)ghvbh