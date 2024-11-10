def remove(item_):
    result = ''.join(char for char in item_ if char in "@#$^")
    return result


text = input().split(',')
clean_list = [item.strip() for item in text]

for item in clean_list:
    if len(item) == 20:
        if any(sym in item for sym in "@#$^"):
            left_side = item[:len(item) // 2]
            right_side = item[len(item) // 2:]
            left_side = remove(left_side)
            right_side = remove(right_side)

            if left_side == right_side and len(left_side) == 10:
                print(f"ticket \"{item}\" - {len(left_side)}{left_side[0:1]} Jackpot!")
            elif left_side == right_side:
                print(f"ticket \"{item}\" - {len(left_side)}{left_side[0:1]}")
        else:
            print(f"ticket \"{item}\" - no match")
    else:
        print("invalid ticket")