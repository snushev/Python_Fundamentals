def calculate_love_score(name1, name2):
    true_num = 0
    love_num = 0
    names = name1 + name2
    for char in names.lower():
        if char in "TRUE":
            true_num += 1
    for char in names.lower():
        if char in "LOVE":
            love_num += 1

    print(f"{true_num}{love_num}")


calculate_love_score("Angela Yu", "Jack Bauer")