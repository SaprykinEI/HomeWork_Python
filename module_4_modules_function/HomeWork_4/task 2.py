def displays_even_number(number_one, number_two):
    '''Функция принимает два числа и отображает чётные числа между ними'''
    for even in range(number_one, number_two):
        if even % 2 == 0:
            even_numbers.append(even)
    return even_numbers


even_numbers = []
displays_even_number(3, 25)
print(even_numbers)


