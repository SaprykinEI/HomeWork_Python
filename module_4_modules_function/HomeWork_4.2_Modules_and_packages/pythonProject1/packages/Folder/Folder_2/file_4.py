from os import path


def file_4_import():
    address = path.abspath('.')
    return f"Я файл 4 из Folder_2 импортирован из: {address}"

if __name__ == "__main__":
     print(f"Я файл 4!")