from sys import path

def file_5_import():
    path.append(r'Z:\Training\Top-school\Home Work\Module4\HomeWork_4.2_Modules_and_packages\pythonProject1\packages\Folder\Folder_2\Folder_3')
    return f"Я файл 5 из Folder_3 импортирован из: {path[0]}"


if __name__ == "__main__":
    print(f"Я файл 5 в пакете!")

