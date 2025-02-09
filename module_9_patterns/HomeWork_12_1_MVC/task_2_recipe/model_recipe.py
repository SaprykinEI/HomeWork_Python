import json


class RecipeModel:

    def __init__(self):
        self.recipe_list = []

    def get_ingredients(self):
        """Получить меню"""
        return self.recipe_list

    def add_recipe(self, name_recipe, author, type_dish,
                   tittle, ingredients: list, kitchen_name, filename):
        """Добавление рецепта"""
        data_recipe = {}
        data_recipe['name_recipe'] = name_recipe
        data_recipe['author'] = author
        data_recipe['type_dish'] = type_dish
        data_recipe['tittle'] = tittle
        data_recipe['ingredients'] = ingredients
        data_recipe['kitchen_name'] = kitchen_name
        self.recipe_list.append(data_recipe)
        self.update_json(filename)

    def update_json(self, filename):
        """Сериализация файлов в json"""
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(self.recipe_list, fp, ensure_ascii=False, indent=2)
