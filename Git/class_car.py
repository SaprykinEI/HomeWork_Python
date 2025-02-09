class Car():
    '''Простая модель автомобиля'''


    def __init__(self, make, model, year):
        '''Инициализирует атрибуты описания автомобиля'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        '''Возвращает аккуратно отформатированное описание'''
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        '''Вывод пробег машины в милях'''
        print(f"This car has {self.odometer_reading} miles on it")


    def update_odometer(self, milieage):
        '''Устанавливает заданное значение на одометре
        При попытке обратной открутке изменения отклоняются'''
        if milieage >= self.odometer_reading:
            self.odometer_reading = milieage
        else:
            print("Одометр скручивать нельзя")

    def increment_odometer(self, miles):
        '''Увеличивает показания одометра с заданным приращением'''
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()




my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.update_odometer(24)
print(my_new_car.read_odometer())



class Battery():
    '''Простая модель акумулятора автомобиля'''

    def __init__(self, battery_size=75):
        '''Инициализирует атрибуты аккумулятора'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Выводит информацию о мощности аккумулятора'''
        print(f"This car has a {self.battery_size}-kwh battery")


    def get_range(self):
        '''Выводит приблизительный запас хода аккумулятоа'''

        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")


print('Хочу создать конфликт!')


print("Хочу спровоцировать конфликт")


print("Какой-то текст")

print("Это мой первый pull-request")
print("Это моя доработка pull-request")

print("Были доработки от других разработчиков")
print("Код для конфликта")

print("Код для разрешения конфликта")
