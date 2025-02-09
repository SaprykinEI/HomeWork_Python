from os import path


def file_3_import():
    address = path.abspath('.')
    return f"Я файл 3 из Folder_2 импортирован из: {address}"

if __name__ == "__main__":
     print(f"Я файл 3!")
