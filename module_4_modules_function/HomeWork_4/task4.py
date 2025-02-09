
def return_min_number(num_first, num_second, num_thirthy, num_fourthy, num_fifty ):
    '''Функция возвращает минимальное число'''

    for number in num_first, num_second, num_thirthy, num_fourthy, num_fifty:
       numbers.append(number)
    min_num = min(numbers)
    return min_num


numbers = []
print(return_min_number(27,33,8,55,100))
