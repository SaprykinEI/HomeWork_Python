cinema_genres = ('Комедия', 'Экшн', 'Пеплум', 'Триллер',)

genres_list = list(cinema_genres)
genres_list[1] = 'Боевик'
genres_list.insert(2, 'Документальный')
cinema_genres = tuple(genres_list)
print(type(cinema_genres))
print(cinema_genres)

string_genres = f"Обновлённые жанры: {', '.join(cinema_genres)}"
print(type(string_genres))
print(string_genres)

