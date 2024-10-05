def data(type_, data):
    if type_ == "int":
        return int(data) * 2
    elif type_ == "real":
        return f"{float(input_data) * 1.5:.2f}"
    elif type_ == "string":
        return f'${data}$'


data_type = input()
input_data = input()
print(data(data_type, input_data))