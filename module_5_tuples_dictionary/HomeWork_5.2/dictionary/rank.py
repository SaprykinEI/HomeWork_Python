import json


def get_rank(answers, json_file):
    """Возвращает ранг пользователя на основе правильных ответов."""

    level_data = json_file[1]["levels"]

    rank = ''
    counting_responses = 0

    for correct in answers.values():
        if correct:
            counting_responses += 1

    print(answers)

    for number, level in level_data.items():
        if counting_responses == int(number):
            rank = level


    return rank

