def get_counts_number(num):
    '''Функция считает кол-во цифр в числе'''
    count_number = len(str(number))
    return count_number


number = int(input("Введите число: "))
len_num = get_counts_number(number)
print(f"В данном числе {len_num} цифр/ы!")