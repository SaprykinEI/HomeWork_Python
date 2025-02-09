from sys import path


def module_second_import():
    path.append(r'Z:\Training\Top-school\Home Work\Module4\HomeWork_4.2_Modules_and_packages\pythonProject1\modules')
    return f"Я второй модуль и импортирован из: {path[0]}"


if __name__ == "__main__":
    print(f"Я второй модуль!")