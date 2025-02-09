import collections
from collections import Counter

# 1.	Напишите функцию, которая принимает на вход список продуктов,
# необходимо вернуть словарь, где ключом является название продукта,
# а значением – его количество (сколько элементов в списке).

#-----------Вариант 1 --------------#
# def product():
#    prod_list = input("Введите список продуктов через пробел: ").split()
#    count = collections.Counter()
#    for word in prod_list:
#       count[word] += 1
#    return count
#
#
# print(product())

#-----------Вариант 2 --------------#

# def product():
#     prod_list = input("Введите список продуктов через пробел: ").split()
#     counter = {}
#
#     for quantity in prod_list:
#         counter[quantity] = counter.get(quantity, 0) + 1
#     return counter
#
# print(product())


# 2.Напишите функцию, которая принимает на вход список чисел,
# необходимо вернуть True, если в списке есть дубликаты и False, если их нет.

#-----------Вариант 1 --------------#

# def double():
#    number = input("Введите список чисел через пробел: ").split()
#    duplicate = len(number) > len(set(number))
#    return duplicate
#
# print(double())


#-----------Вариант 2 --------------#

# def double():
#     num_list = input("Введите список чисел через пробел: ").split()
#     num_set = set(num_list)
#     if len(num_list) == len(num_set):
#         print(False)
#     else:
#         print(True)
#
#
#
# print(double())


# 3.Напишите функцию, которая принимает на вход принимает словарь, в котором ключ – один символ,
# а значение – число. Необходимо вернуть строку, в которой будет последовательность из букв-ключей,
# каждая из которых будет длиной, указанной в значении. Например, из словаря {‘a’: 3, ‘b’: 2}
# можно сделать строки “aaabb” или “bbaaa” (порядок символов не важен).


#-----------Вариант 1 --------------#

# def func(x):
#
#     dictionary = Counter(x)
#     new_str = ''.join(list(dictionary.elements()))
#     return new_str
#
#
# print(func({'a': 3, 'b': 2}))


#-----------Вариант 2 -----Нашел в интернете---------#


# def func(hand: dict[str, int]) -> None:
#    for letter in hand.keys():
#       for i in range(hand[letter]):
#          print(letter, end="")
#
# func({'м': 7, 'и': 3,})



# 4.Напишите функцию, которая на вход получает словарь продуктов, в котором ключ – название продукта,
# а значение – словарь с ключами ‘name’, ‘cost’, ‘kg’. Необходимо вернуть кортеж,
# содержащий всю информацию о самом дорогом товаре. Например, дается словарь:
# {
# ‘apple’: {‘name’: ‘Яблоко зеленое’, ‘cost’: 37, ‘kg’: 24},
# ‘pineapple’: {‘name’: ‘Ананас’, ‘cost’: 50, ‘kg’: 20}
# }
# В данном случае вернуть надо кортеж (‘pineapple’, ‘Ананас’, 50, 20), т.к. стоимость 50 – наибольшая.


# dict_fruit = {
#     'apple': {'name': 'Яблоко зеленое', 'cost': 37, 'kg': 24},
#     'pinapple': {'name': 'Ананас', 'cost': 50, 'kg': 20}
#     }
# list_fruit = []
#
# def fr():
#     if dict_fruit['apple']['cost'] < dict_fruit['pinapple']['cost']:
#         del dict_fruit['apple']
#
#     for d in dict_fruit.keys():
#         list_fruit.append(d)
#     for b in dict_fruit['pinapple'].values():
#         list_fruit.append(b)
#
#     tuple_fruit = tuple(list_fruit)
#     return tuple_fruit
#
# print(fr())



#--------------------------------
products = {
    'apple': {'name': 'Яблоко зеленое', 'cost': 37, 'kg': 24},
    'pinapple': {'name': 'Ананас', 'cost': 50, 'kg': 20}
    }


def mostExpensiveProduct(x):
    keyExpensive = list(products.keys())[0]


    for product in products.keys():
        if products[product]['cost'] > products[keyExpensive]['cost']:
            keyExpensive = product
            

    result = (keyExpensive,
              products[keyExpensive]['name'],
              products[keyExpensive]['cost'],
              products[keyExpensive]['kg'])
    return result

print(mostExpensiveProduct(products))


#-----------Прописывал условия для того, если яблоко дороже ананаса,
# все работает без функции, но не знаю как добавить это в функцию --------------#


# elif dict_fruit['apple']['cost'] > dict_fruit['pinapple']['cost']:
#     del dict_fruit['pinapple']
#
#     for d in dict_fruit.keys():
#         list_fruit.append(d)
#     for b in dict_fruit['apple'].values():
#         list_fruit.append(b)
#
#     tuple_fruit = tuple(list_fruit)
#     print(tuple_fruit)
#
# elif dict_fruit['apple']['cost'] == dict_fruit['pinapple']['cost']:
#     print(f"Стоимость яблок и ананасов равна {dict_fruit['apple']['cost']}, видимо в Бразилии хороший урожай ананасов!")



# 5.*Напишите функцию, которая получает строку и словарь, в котором ключ – слово, а значение – количество раз,
# которое надо удалить это слово в полученной строке. Необходимо вернуть отредактированную строку.
# Например, строка – ‘hello hello hello I want to tell you about our forest and our town’,
# словарь – {‘hello’: 2, ‘our’: 1, ‘you’: 1}, тогда результатом будет строка:
# ‘hello I want to tell about forest and our town’



#---------Решил, не уверен что правильно, так как словарь у меня не фигурирует в решение.
# Но результат выводит какой просит условие задачи



# string = 'hello hello hello I want to tell you about our forest and our town'
# dict_dict = {'hello': 2, 'our': 1, 'you': 1}
# new_string = string.split()
# list_other = []
#
# def dell():
#     for z in new_string:
#         if (string.count(z) >= 1 and (z not in list_other)):
#             list_other.append(z)
#             st = ' '.join(list_other)
#     return st
#
#
#
# print(dell())



