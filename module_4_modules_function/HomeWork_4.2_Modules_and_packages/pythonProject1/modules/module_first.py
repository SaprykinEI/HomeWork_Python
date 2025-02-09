from os import path


def module_first_import():
    address = path.abspath('.')
    return f"Я первый модуль и импортирован из: {address}"

if __name__ == "__main__":
     print(f"Я первый модуль!")




