first_row = list(map(int, input().split()))
second_row = list(map(int, input().split()))
third_row = list(map(int, input().split()))

if 1 in first_row + 1 in second_row + 1 in third_row >= 3 and \
        2 in first_row + 2 in second_row + 2 in third_row < 3:
    print("First player won")
elif "1" in first_row + "1" in second_row + "1" in third_row < "111" and \
        "2" in first_row + "2" in second_row + "2" in third_row == "222":
    print("Second player won")
else:
    print("Draw!")