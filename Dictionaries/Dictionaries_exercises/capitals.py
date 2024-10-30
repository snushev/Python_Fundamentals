countries = input().split(', ')
capitals = input().split(', ')

current = zip(countries, capitals)

dict_ = {country: capital for country, capital in current}

for country, capital in dict_.items():
    print(f'{country} -> {capital}')