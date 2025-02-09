from sys import path
def func_1_2_import():
    path.append(r'Z:\Training\Top-school\Home Work\Module4\HomeWork_4.2_Modules_and_packages\pythonProject1\packages\Folder')
    return f"Я файл 2 из Folder импортирован из: {path[0]}"


if __name__ == "__main__":
    print(f"Я файл 2 в пакете!")
