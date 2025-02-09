import json


class ShoesModel:
    """Модель обуви"""

    def __init__(self):
        self.shoes_are_available = []

    def get_shoes(self):
        """Поучить список обуви"""
        return self.shoes_are_available

    def add_shoes(self, type_shoes, assortment, color,
                  price, brand, size: list, filename):
        """Добавление обуви"""
        data = {}
        data['type_shoes'] = type_shoes
        data['assortment'] = assortment
        data['color'] = color
        data['price'] = price
        data['brand'] = brand
        data['size'] = size
        self.shoes_are_available.append(data)
        self.update_json(filename)

    def update_json(self, filename):
        """Сериализация файлов в json"""
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(self.shoes_are_available, fp, ensure_ascii=False,
                      indent=2)