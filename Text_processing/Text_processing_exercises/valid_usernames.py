usernames = input().split(', ')
usernames1 = [name for name in usernames if 3 <= len(name) <= 16]

for name in usernames1:
    if all(char.isalnum() or char in '-_' for char in name):
        print(name)
