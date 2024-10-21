def family(years, km):
    return (km // 3000) * 12 + (50 - years * 5)


def heavyduty(years, km):
    return (km // 9000) * 14 + (80 - years * 8)


def sports(years, km):
    return (km // 2000) * 18 + (100 - years * 9)


def main():
    vehicles_list = input().split('>>')
    total_tax = 0

    for current_car in vehicles_list:
        car_info = current_car.split(' ')
        car_type = car_info[0]
        years_fot_tax = int(car_info[1])
        kilometers = int(car_info[2])

        if car_type == 'family':
            tax = family(years_fot_tax, kilometers)
            total_tax += tax
            print(f'A {car_type} car will pay {tax:.2f} euros in taxes.')
        elif car_type == 'heavyDuty':
            tax = heavyduty(years_fot_tax, kilometers)
            total_tax += tax
            print(f'A {car_type} car will pay {tax:.2f} euros in taxes.')
        elif car_type == 'sports':
            tax = sports(years_fot_tax, kilometers)
            total_tax += tax
            print(f'A {car_type} car will pay {tax:.2f} euros in taxes.')
        else:
            print('Invalid car type.')

    print(f'The National Revenue Agency will collect {total_tax:.2f} euros in taxes.')


main()
