def new_sum(*args):
    sum_ = 0
    for num in args:
        sum_ += num
    return sum_

print(new_sum(1, 5, 3, 4, 5))

###------------###

def longest_word(*args):
    print(args)
    print(type(args))
    leader = ""

    for word in args:
        if type(word) is str:
            if len(word) > len(leader):
                leader = word
    return leader


print(longest_word("Python", "Java", 3, [], "Programming"))


###------------###


def remove_from_string(string, *args):
    for symbol in args:
        string = string.replace(symbol, '')

    return string

print(remove_from_string("Смотри! Мы, можем удалить: все знаки препинания сразу. Или нет?", "!", "?", ".", ",", ":"))


###------------###

def get_personal_data(**kwargs):
    print(type(kwargs))
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['surname'])
    print(kwargs['age'])
    print(kwargs['phone'])


get_personal_data(name="Evgeniy", surname="Saprykin", age=32, phone='+79304126946')


###------------###

def planet_space_address(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)

planet_space_address(planet="Земля", star="Солнце", galaxy="Млечный", age=round(4.543e9))


###------------###

def my_space_address(*args, **kwargs):
    if args:
        for item in args:
            print(item)
    if kwargs:
        for key, value in kwargs.items():
            print(key, value)


my_space_address("Evgeniy", 32, planet="Земля", star='Солнце')


###------------###

data_list = [60, 2]
data_tuple = [50, 3]


def calculate(v, t):
    way = v * t
    return way


print(f"Распаковка списка: {calculate(*data_list)}")
print(f"Распаковка кортежа: {calculate(*data_tuple)}")