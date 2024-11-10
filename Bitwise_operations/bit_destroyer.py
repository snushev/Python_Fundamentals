num = int(input())
index_to_convert = int(input())

binary_representation = bin(num)
binary_list = list(binary_representation)
binary_list[-index_to_convert - 1] = "0"

binary_num = "".join(binary_list)
decimal_representation = int(binary_num, 2)

print(decimal_representation)