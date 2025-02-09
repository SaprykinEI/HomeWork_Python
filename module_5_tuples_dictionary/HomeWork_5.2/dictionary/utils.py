def base_program(question):
    '''Задаёт вопросы, полученные ответы добавляет в словарь'''

    answers = {}
    for key, value in question.items():
        print(f"Переведите слово: {key.title()}")
        print("Подсказки: ")
        print(f"Это слово состоит из {len(value)} букв")
        print(f"Первая буква слова: {value[0].title()}\n")

        your_answer = input("Введите ваш ответ: ").replace(' ', '').lower()

        if your_answer == value:
            print(f"Верно, {key.title()} - это {value}\n")
            answers[key] = True

        else:
            print(f"Неверно, {key.title()} - это {value}\n")
            answers[key] = False

    return answers