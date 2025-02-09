import re

def get_reg_data():
    """Возвращает список паттернов для проверки данных."""

    reg_name = re.compile(r'^[A-Za-zA-Яа-яЁё]+$')
    reg_surname = re.compile(r'^[A-Za-zA-Яа-яЁё]+$')
    reg_phone = re.compile(r'^[+]\d{1,3}\(\d{1,3}\)(\d{7})$')
    reg_mail = re.compile(r'^[A-Za-z0-9_]+@yandex\.ru$')

    patterns_list = [reg_name, reg_surname, reg_phone, reg_mail]
    return patterns_list


def reg_check(user_data, reg_pattern, user_list, data_to_check=None):
    while True:
        if reg_pattern.match(user_data):
            if len(user_list) > 0 and data_to_check:
                if not check_unique_data(user_data, data_to_check):
                    user_data = input("Введите данные: ")
                    continue
        else:
            print("Ввод некорректен\n Повторите ввод!")
            user_data = input("Введите данные: ")
            continue
        print(f'{user_data} - данные приняты!')
        return user_data


def check_unique_data(user_data, data_to_check):
    if user_data in data_to_check:
        print("Такие данные уже есть".center(30,'!'))
        print("Введите уникальные данные!")
        return False
    else:
        return True