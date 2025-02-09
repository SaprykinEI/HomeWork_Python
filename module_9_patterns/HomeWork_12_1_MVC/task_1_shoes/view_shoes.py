class ShoesView:

    def __init__(self, controller):
        self.controller = controller

    def display_default_action(self):
        print(self.controller.get_default_action())

    def display_shoes_auth(self, user_role='user'):
        result = self.controller.get_shoes_auth(user_role)

        if result == "Forbidden!":
            print(result)
            return

        if not result:
            print("Нет данных!")
            return

        for shoe in result:
            print(f"Тип: {shoe['type_shoes']}, Вид: {shoe['assortment']}, "
                  f"Цвет: {shoe['color']}, Цена: {shoe['price']}, "
                  f"Бренд: {shoe['brand']}, Размер: {shoe['size']}")

    def display_only_assortment_list(self):
        result = self.controller.only_assortment_list()
        if result:
            print("Наш ассортимент: ")
            for item in result:
                print(item)
            print()
        else:
            print("\nОбуви нет!")

    def display_only_brand_list(self):
        result = self.controller.only_brand_list()
        if result:
            print("Список Брендов: ")
            for item in result:
                print(item)
            print()
        else:
            print("\nБрендов нет!")

    def display_only_color_list(self):
        result = self.controller.only_color_list()
        if result:
            print("Список обуви по цветам: ")
            for item in result:
                print(item)
            print()
        else:
            print("\nТаких расцветок нет!")

    def display_all_data_list(self):
        result = self.controller.get_all_shoes_list()
        if result:
            print(result)
        else:
            print("Данных нет!")

    def display_add_shoes(self, type_shoes, assortment, color,
                  price, brand, size: list, filename, user_role='user'):
        if not isinstance(price, int):
            print("Недопустимый тип цены")
            return
        result = self.controller.add_mark(type_shoes, assortment, color,
                  price, brand, size, filename, user_role)
        if result == 'Forbidden':
            print("Forbidden")
        else:
            print(result)
