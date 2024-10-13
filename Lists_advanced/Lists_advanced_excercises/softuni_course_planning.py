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
        title_index = titles_list.index(title)
        if title_index + 1 in range(len(titles_list)):
            if "Exercise" in titles_list[title_index + 1]:
                titles_list.pop(title_index + 1)
        titles_list.remove(title)
    return titles_list


def swap_lesson(list_of_lessons, first_lesson, second_lesson):
    if first_lesson in list_of_lessons and second_lesson in list_of_lessons:
        first_position = list_of_lessons.index(first_lesson)
        second_position = list_of_lessons.index(second_lesson)
        first_lesson_has_exercise = False
        second_lesson_has_exercise = False
        if first_position + 1 in range(len(list_of_lessons)):
            first_lesson_has_exercise = "Exercise" in list_of_lessons[first_position + 1]
        if second_position + 1 in range(len(list_of_lessons)):
            second_lesson_has_exercise = "Exercise" in list_of_lessons[second_position + 1]
        # Swap lessons
        list_of_lessons[first_position], list_of_lessons[second_position] = list_of_lessons[second_position], \
                                                                            list_of_lessons[first_position]
        # Swap exercises
        if first_lesson_has_exercise and second_lesson_has_exercise:
            list_of_lessons[first_position + 1], list_of_lessons[second_position + 1] = \
                list_of_lessons[second_position + 1], list_of_lessons[first_position + 1]
        elif not first_lesson_has_exercise and second_lesson_has_exercise:
            # list_of_lessons.insert(first_position + 1, list_of_lessons[second_position + 1])
            # list_of_lessons.pop(second_position + 1)
            list_of_lessons.insert(first_position + 1, list_of_lessons.pop(second_position + 1))
        elif first_lesson_has_exercise and not second_lesson_has_exercise:
            # list_of_lessons.insert(second_position +1, list_of_lessons[first_position + 1])
            # list_of_lessons.pop(first_position + 1)
            list_of_lessons.insert(second_position + 1, list_of_lessons.pop(first_position + 1))
    return list_of_lessons


def exercise_titles(title_list: list, title: str) -> list:
    exercise_name = f"{title}-Exercise"
    if title in title_list and exercise_name not in title_list:
        title_index = title_list.index(title)
        title_list.insert(title_index + 1, exercise_name)
    elif title not in title_list:
        title_list.append(title)
        title_list.append(exercise_name)
    return title_list


lessons = input().split(', ')
command = input().split(':')


while len(command) > 1:
    action = command[0]
    lesson_title = command[1]

    if action == "Add":
        lessons = add_title(lessons, lesson_title)
    elif action == "Insert":
        index = int(command[2])
        lessons = insert_title(lessons, lesson_title, index)
    elif action == "Remove":
        lessons = remove_title(lessons, lesson_title)
    elif action == "Swap":
        lesson_2_title = command[2]
        lessons = swap_lesson(lessons, lesson_title, lesson_2_title)
    elif action == "Exercise":
        lessons = exercise_titles(lessons, lesson_title)
    command = input().split(':')

for index, lesson in enumerate(lessons):
    print(f"{index + 1}.{lesson}")