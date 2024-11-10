file_name = input().split("\\")[-1]
file_extension = file_name.split('.')[-1]

print(f"File name: {file_name.split('.')[0]}")
print(f"File extension: {file_extension}")
