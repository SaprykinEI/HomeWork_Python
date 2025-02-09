
def make_product_number(one_num, two_num):
    '''Функция возвращает произведение чисел'''
    try:
        if 5 <= one_num <= 25 and 6 <= two_num <= 25 and one_num < two_num:
            prod_num = one_num * two_num

        elif 5 <= one_num <= 25 and 5 <= two_num <= 25 and one_num > two_num:
            three_num = one_num
            one_num = two_num
            two_num = three_num

            print(one_num, two_num) # Проверка изменений
            prod_num = one_num * two_num

        else:
            print("Введите числа в диапозоне от 5 до 25")

        return prod_num

    except Exception:
        print("Введите числа в диапозоне от 5 до 25")


prod_num = make_product_number(6, 5)
print(f"Произведение чисел равно {prod_num}")
