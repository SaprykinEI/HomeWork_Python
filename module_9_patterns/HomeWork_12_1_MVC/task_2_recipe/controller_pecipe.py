class RecipeController:

    def __init__(self, model):
        self.model = model

    @classmethod
    def get_default_recipe(cls):
        return "Добро пожаловать в книгу рецептов"

    def get_recipe_auth(self, user_role='user'):
        """Аутентификация для получения списка обуви"""
        if user_role in ['admin', 'user']:
            if self.model.get_ingredients():
                return self.model.get_ingredients()
            return None

    def get_only_name_recipe(self):
        name_list = []
        data = self.model.get_ingredients()
        if data:
            for name in data:
                name_list.append(name['name_recipe'])
            return name_list
        return None

    def get_only_author_recipe(self):
        author_list = []
        data = self.model.get_ingredients()
        if data:
            for author in data:
                author_list.append(author['author'])
            return author_list
        return None

    def get_only_type_dish_recipe(self):
        type_dish_list = []
        data = self.model.get_ingredients()
        if data:
            for type in data:
                type_dish_list.append(type['type_dish'])
            return type_dish_list
        return None

    def get_only_tittle_recipe(self):
        tittle_list = []
        data = self.model.get_ingredients()
        if data:
            for tittle in data:
                tittle_list.append(tittle['tittle'])
            return tittle_list
        return None

    def get_only_ingredients_recipe(self):
        ingredients_list = []
        data = self.model.get_ingredients()
        if data:
            for ingredient in data:
                ingredients_list.append(ingredient['ingredients'])
            return ingredients_list
        return None

    def get_only_kitchen_name_recipe(self):
        kitchen_name_list = []
        data = self.model.get_ingredients()
        if data:
            for name in data:
                kitchen_name_list.append(name['kitchen_name'])
            return kitchen_name_list
        return None

    def get_all_recipe_list(self):
        if self.model.get_ingredients():
            return (self.get_only_name_recipe(), self.get_only_author_recipe(),
                    self.get_only_type_dish_recipe(), self.get_only_tittle_recipe(),
                    self.get_only_ingredients_recipe(), self.get_only_kitchen_name_recipe())
        return None

    def add_recipe(self, name_recipe, author, type_dish,
                   tittle, ingredients: list, kitchen_name,
                   filename, user_role='user'):
        if user_role != 'admin':
            return 'Forbidden'
        self.model.add_recipe(name_recipe, author, type_dish, tittle, ingredients, kitchen_name, filename)
        return "Рецепт успешно добавлен"