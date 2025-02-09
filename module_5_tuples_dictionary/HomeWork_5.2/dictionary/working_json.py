import json

def create_json_file(file_path, test_answer):
    '''Создаёт json файл с ответами пользователя'''
    with open(f'{file_path}.json', 'w', encoding='UTF-8') as file:
        json.dump(test_answer, file, indent=2)
    return file_path


def get_unpacking_json() -> list:
    '''Распаковывает json файл'''
    with open('questions.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

