animals = input().split(", ")

for index, animal in enumerate(animals):
    if len(animals) - index == 1 and animal == "wolf":
        print("Please go away and stop eating my sheep")
    elif animal == "wolf":
        print(f'Oi! Sheep number {len(animals) - index - 1}! You are about to be eaten by a wolf!')
