def check_palindrome_number(number):
    '''Проверка числа на палиндром'''

    new_num = str(number)
    reversed_num = new_num[::-1]

    if new_num == reversed_num:
        return print("Это палиндром")
    else:
        return print("Это не палиндром")


num = int(input("Введите число: "))
numbers = check_palindrome_number(num)
print(numbers)