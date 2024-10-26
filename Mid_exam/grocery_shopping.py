def important(products_list, commands):
    if product in products_list:
        products_list.remove(product)
        products_list.insert(0, product)
    else:
        products_list.insert(0, product)
    return products_list


def add(products_list, commands):
    if product not in products_list:
        products_list.append(product)
    else:
        print('The product is already in the list.')
    return products_list


def swap(products_list, commands):
    if product not in products:
        print(f"Product {product} missing!")
    elif product2 not in products:
        print(f"Product {product2} missing!")
    else:
        index1 = products_list.index(product)
        index2 = products_list.index(product2)
        products_list[index1], products_list[index2] = products_list[index2], products_list[index1]


    return products_list


def remove(products_list, commands):
    if product in products_list:
        products_list.remove(product)
    else:
        print(f"Product {product} isn't in the list.")
    return products_list


products = input().split('|')

while True:
    command = input()

    if command == 'Shop!':
        break
    elif command == 'Reversed':
        products.reverse()
    else:
        command_parts = command.split('%')
        action = command_parts[0]
        product = command_parts[1]

        if action == "Important":
            products = important(products, command)
        elif action == "Add":
            products = add(products, command)
        elif action == "Swap":
            product2 = command_parts[2]
            products = swap(products, command)
        elif action == "Remove":
            products = remove(products, command)

for index, item in enumerate(products):
    print(f"{index + 1}. {item}")