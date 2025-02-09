genres_books = 'Роман', 'Новелла', 'Фэнтези', 'Научная Фантастика'
tuples_nums = (3, 7, 9, 1, 6, 8, 2, 5, 4)

print(len(genres_books))
print(len(tuples_nums))

print(max(genres_books))
print(max(tuples_nums))

print(min(genres_books))
print(min(tuples_nums))

print(sum(tuples_nums))

sorted_books = tuple(sorted(genres_books))
print(sorted_books)
sorted_nums = tuple(sorted(tuples_nums))
print(sorted_nums)

print(tuple(sorted(genres_books, reverse=True)))
print(tuple(sorted(tuples_nums, reverse=True)))

genres_list = list(genres_books)
genres_list.sort()
genres_books = tuple(genres_list)
print(genres_books)
print(type(genres_books))

num_list = list(tuples_nums)
num_list.sort()
tuples_nums = tuple(num_list)
print(tuples_nums)
print(type(tuples_nums))

genres_list = list(genres_books)
genres_list.sort(reverse=True)
genres_books = tuple(genres_list)
print(genres_books)
print(type(genres_books))

num_list = list(tuples_nums)
num_list.sort(reverse=True)
tuples_nums = tuple(num_list)
print(tuples_nums)
print(type(tuples_nums))