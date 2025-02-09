import threading
import random
import time
import math
from sympy import isprime

numbers = []
path = r'files\random_number.txt'
path_prime = r'files\primes_number.txt'
path_factorial = r'files\factorial_number.txt'

event = threading.Event()



def random_numbers():
    global numbers
    print("Генерация списка...")
    numbers = [random.randint(1, 100) for _ in range(10)]
    time.sleep(1)
    print(f"Список создан: {numbers}")
    event.set()

    with open(path, 'w', encoding='utf-8') as file:
        for num in numbers:
            file.write(f"{num}\n")
        print("Список чисел записан в файл")


def search_prime_numbers():
    event.wait()
    primes = [num for num in numbers if isprime(num)]
    with open(path_prime, 'w') as f:
        for prime in primes:
            f.write(f"{prime}\n")
    print(f"Простые числа: {primes}")


def calculate_factorials():
    event.wait()
    factorials = [math.factorial(num) for num in numbers]
    with open(path_factorial, 'w') as f:
        for fact in factorials:
            f.write(f"{fact}\n")
    print(f"Факториалы чисел: {factorials}")

if __name__ == '__main__':

    thread1 = threading.Thread(target=random_numbers())
    thread2 = threading.Thread(target=search_prime_numbers())
    thread3 = threading.Thread(target=calculate_factorials())

    thread1.start()
    thread2.start()
    thread3.start()

    thread1.join()
    thread2.join()
    thread3.join()