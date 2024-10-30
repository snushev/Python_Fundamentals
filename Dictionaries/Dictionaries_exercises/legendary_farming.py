items = {"shards": 0, "fragments": 0, "motes": 0}
data = input().split()
unique_item = " "
unique_found = False
while not unique_found:
    for index in range(0, len(data), 2):
        item = data[index + 1].lower()
        quantity = int(data[index])
        if item not in items:
            items[item] = quantity
        else:
            items[item] += quantity
        if items['shards'] >= 250:
            unique_item = "Shadowmourne"
            items['shards'] -= 250
            unique_found = True
            break
        elif items['fragments'] >= 250:
            unique_item = "Valanyr"
            items['fragments'] -= 250
            unique_found = True
            break
        elif items['motes'] >= 250:
            unique_item = "Dragonwrath"
            items['motes'] -= 250
            unique_found = True
            break
    if not unique_found:
        data = input().split()

print(f'{unique_item} obtained!')

for i in items:
    print(f"{i}: {items[i]}")
