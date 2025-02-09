class ControllerShoes:

    def __init__(self, model):
        self.model = model

    @classmethod
    def get_default_action(cls):
        return "Добро пожаловать в каталог обуви"

    def get_shoes_auth(self, user_role='user'):
        """Аутентификация для получения списка обуви"""
        if user_role in ['admin', 'user']:
            if self.model.get_shoes():
                return self.model.get_shoes()
            return None
        return 'Forbidden!'

    def only_assortment_list(self):
        shoes_assortment_list = []
        data = self.model.get_shoes()
        if data:
            for shoe in data:
                shoes_assortment_list.append(shoe['assortment'])
            return shoes_assortment_list
        return None

    def only_brand_list(self):
        shoes_brand_list = []
        data = self.model.get_shoes()
        if data:
            for shoe in data:
                shoes_brand_list.append(shoe['brand'])
            return shoes_brand_list
        return None

    def only_color_list(self):
        shoes_color_list = []
        data = self.model.get_shoes()
        if data:
            for shoe in data:
                shoes_color_list.append(shoe['color'])
            return shoes_color_list
        return None

    def get_all_shoes_list(self):
        if self.model.get_shoes():
            return self.only_assortment_list(), self.only_brand_list(), self.only_color_list()
        return None

    def add_shoes(self, type_shoes, assortment, color,
                  price, brand, size: list, filename, user_role='user'):
        if user_role != 'admin':
            return 'Forbidden'
        elif not isinstance(price, int):
            return "Недопустимый тип цены"
        self.model.add_shoes(type_shoes, assortment, color, price, brand, size, filename)
        return "Обувь успешно добавлена"
