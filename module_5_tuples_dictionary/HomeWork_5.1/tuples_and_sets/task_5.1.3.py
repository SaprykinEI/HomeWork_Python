my_bag = {'Палатка', 'Спальник', 'Горелка', 'Газ', 'Удочка', 'Шатёр', 'Топор', 'Power Bank', 'Питьевая вода', 'Ружье'}
other_bag = {'Лекарства', 'Рация', 'Палатка', 'Сигнальная ракета', 'Вода', 'Надувная Лодка', 'Нож', 'Спички', 'Удочка', 'Крючок'}

duplicate_bag = my_bag.intersection(other_bag)
print(duplicate_bag)

new_bag = my_bag.difference(other_bag)
print(new_bag)

other_new_bag = other_bag.difference(my_bag)
print(other_new_bag)

our_bag = my_bag.union(other_bag)
print(our_bag)