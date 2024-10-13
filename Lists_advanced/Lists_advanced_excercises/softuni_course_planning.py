def add_title(titles_list: list, title: str) -> list:
    if title not in titles_list:
        titles_list.append(title)
        return titles_list


def insert_title(titles_list: list, title: str, index_of_insert: int) -> list:
    if title not in titles_list:
        titles_list.insert(index_of_insert, title)
        return titles_list


def remove_title(titles_list: list, title: str) -> list:
    if title in titles_list:
        titles_list.remove(title)
    return titles_list


def swap_titles(titles_list: list, title1: str, title2: str) -> list:
    if title1 in titles_list and title2 in titles_list:
        titles_list[titles_list.index(title1)], titles_list[titles_list.index(title2)] = titles_list[titles_list.index(title2)], titles_list[titles_list.index(title1)]
    return titles_list


def exercise_titles(title_list: list, title: str) -> list:
    


initial_schedule = input().split(', ')
command = input().split(':')

while True:
    if command[0] == "course start":
        break
