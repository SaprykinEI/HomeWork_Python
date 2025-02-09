import os


def get_absolute_path(path):
    '''Возвращает нормализованный абсолютный путь к файлу'''
    return print(f"Нормализованный абсолютный путь: {path}")


get_absolute_path(os.path.normpath(r'Z:/Training/Top-school/Home Work/module_6/HomeWork_01_files/data_path_1/test_file_1.txt'))


def show_contents_folder(path_project):
    '''Функция показывает содержимое папок вашего проекта'''
    for path, dirnames, filenames in os.walk(path_project):
        print(f"path - {path}")
        print(f"dirnames - {dirnames}")
        print(f"filenames - {filenames}")

    return path_project


print(show_contents_folder(os.path.normpath(r'Z:\Training\Top-school\Home Work\module_6\HomeWork_01_files')))


def composes_the_path(*args):
    '''Функция составляет абсолютный путь'''
    composes_path = os.path.join(*args)
    return composes_path

new_absolute_path = ('Z:\\', 'Training', 'Top-school', 'Home Work', 'module_6', 'HomeWork_01_files', 'data_path_2', 'test_file_3.txt\n')
print(composes_the_path(*new_absolute_path))


def creates_a_folder(name):
    '''Функуия создаёт папку'''
    try:
        base_directory = '.'
        test_directory = 'data_path_2'
        new_directory = name

        path_dir_new_dir = os.path.join(base_directory, test_directory, new_directory)

        new_folder = os.mkdir(path_dir_new_dir)
        print(f"Папка '{name}' создана в директории: {path_dir_new_dir}")
        return new_folder

    except FileExistsError:
        print("Папки с таким именем не существует, попробуйте выбрать другое имя!")

# creates_a_folder('new_folder2')



def delete_a_folder(name_folder):
    '''Функция удаляет папку'''

    try:
        base_directory = '.'
        test_directory = 'data_path_2'
        new_directory = name_folder

        path_dir_new_dir = os.path.join(base_directory, test_directory,
                                        new_directory)

        del_folder = os.rmdir(path_dir_new_dir)
        print(f"Папка '{name_folder}' была удалена из директории: {path_dir_new_dir}")
        return del_folder

    except FileNotFoundError:
        print("Папки с таким именем не существует, попробуйте выбрать другую папку!")


delete_a_folder('new_folder14')



