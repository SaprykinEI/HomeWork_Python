from datetime import datetime

def time():
    text = input("Введите текст: ")
    my_datetime = datetime.now().strftime('[%d-%m-%Y %H:%M:%S], ') + text
    return my_datetime


print(time())