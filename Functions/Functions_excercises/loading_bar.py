def loading_bar(progress_number):
    if progress_number == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    loaded_percents_as_digits = number // 10
    not_loaded_percents_as_digits = 10 - loaded_percents_as_digits
    return f"{number}% [{'%' * loaded_percents_as_digits}{'.' * not_loaded_percents_as_digits}]\nStill loading..."


number = int(input())
print(loading_bar(number))

