def get_square(side_length, symbol, booled):
    '''Функция создаёт квадрат пустой\заполненный в зависимости от значения'''
    if booled:
        for i in range(side_length):
            print(symbol * side_length)
    else:
        print(symbol * side_length)
        for i in range(side_length - 2):
            print(symbol + ' ' * (side_length - 2) + symbol)
        print(symbol * side_length)


get_square(3, '$', False)