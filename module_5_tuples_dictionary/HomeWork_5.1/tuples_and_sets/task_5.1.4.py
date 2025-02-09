cinema_genres = ["комедия", "экшн", "пеплум", "триллер", "комедия", "пеплум"]

cinema_genres_set = set(cinema_genres)
cinema_genres_set.add('Исторический')
cinema_genres_set.add('Документальный')
print(cinema_genres_set)
print(type(cinema_genres_set))

cinema_genres_set.remove('пеплум')
cinema_genres_set.remove('экшн')
delete_genres = cinema_genres_set.pop()

print(f'Удалили жанр: {delete_genres}')
print(cinema_genres_set)


cinema_genres = list(cinema_genres_set)
print(cinema_genres)
print(type(cinema_genres))