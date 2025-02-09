from utils import get_reg_data, reg_check

users_list = []
check_phones_list = []
check_emails_lists = []
check_unique_list = [None, None, check_phones_list, check_emails_lists]

data_types = ['имя', 'фамилия', 'телефон', 'email']
reg_patterns_list = get_reg_data()

while len(users_list) < 3:
    user_data_list = []
    data_counter = 0

    while data_counter < 4:
        user_data = input(f"Введите ваши данные {data_types[data_counter]}: ")
        user_data_ok = reg_check(user_data, reg_patterns_list[data_counter], users_list, check_unique_list[data_counter])
        if user_data_ok:
            data_counter += 1
            user_data_list.append(user_data_ok)
            pass
        else:
            continue


    users_list.append(user_data_list)
    check_phones_list.append(user_data_list[2])
    check_emails_lists.append(user_data_list[3])
    print()

[print(user) for user in users_list]

