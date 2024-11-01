command = input()
dict_ = {}
while command != "End":
    company_name, id_ = command.split(' -> ')
    if company_name not in dict_:
        dict_[company_name] = []
    if id_ not in dict_[company_name]:
        dict_[company_name].append(id_)
    command = input()

for company in dict_:
    print(company)
    for id_ in dict_[company]:
        print(f'-- {id_}')
