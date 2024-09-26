command = input()
coffee = 0
while not command == "END":
    if command in ("coding", "dog", "cat", "movie"):
        coffee += 1
    elif command in ("CODING", "DOG", "CAT", "MOVIE"):
        coffee += 2
    command = input()
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)