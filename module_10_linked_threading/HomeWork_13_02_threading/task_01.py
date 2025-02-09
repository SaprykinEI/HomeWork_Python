import threading
import random
import time

numbers = []
event = threading.Event()


def list_numbers():
    global numbers
    print("Генерация списка...")
    numbers = [random.randint(1, 100) for _ in range(10)]
    time.sleep(1)
    print(f"Список создан: {numbers}")
    event.set()



def calculate_sum():
    event.wait()
    total = sum(numbers)
    print(f"Сумма значений равна: {total}\n")


def calculate_average():
    event.wait()
    average = sum(numbers) / len(numbers)
    print(f"Среднее арифметическое: {average:.2f}")


thread1 = threading.Thread(target=list_numbers)
thread2 = threading.Thread(target=calculate_sum)
thread3 = threading.Thread(target=calculate_average)

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()