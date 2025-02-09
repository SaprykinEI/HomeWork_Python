class RecipeView:

    def __init__(self, controller):
        self.controller = controller

    def display_default_recipe(self):
        print(self.controller.get_default_recipe())

    def display_recipe_auth(self, user_role='user'):
        result = self.controller.get_recipe_auth(user_role)

        if result == 'Forbidden!':
            print(result)
            return

        if not result:
            print("Нет данных!")
            return

        for data in result:
            print(f"Наименование: {data['name_recipe']}, Автор: {data['author']},"
                  f"Тип блюда: {data['type_dish']}, Описание: {data['tittle']},"
                  f"Ингридиенты: {data['ingredients']}, Страна: {data['kitchen_name']}")

    def display_only_name_recipe(self):
        result = self.controller.get_only_name_recipe()
        if result:
            print("Наименования блюд:")
            for name in result:
                print(name)
            print()
        else:
            print("\nРецептов нет")

    def display_only_author_recipe(self):
        result = self.controller.get_only_author_recipe()
        if result:
            print("Авторы рецептов:")
            for name in result:
                print(name)
            print()
        else:
            print("\nРецептов нет")

    def display_only_type_dish_recipe(self):
        result = self.controller.get_only_type_dish_recipe()
        if result:
            print("Тип блюд:")
            for name in result:
                print(name)
            print()
        else:
            print("\nРецептов нет")

    def display_only_tittle_recipe(self):
        result = self.controller.get_only_tittle_recipe()
        if result:
            print("Описание рецепта:")
            for name in result:
                print(name)
            print()
        else:
            print("\nРецептов нет")

    def display_only_ingredients_recipe(self):
        result = self.controller.get_only_ingredients_recipe()
        if result:
            print("Ингридиенты:")
            for name in result:
                print(name)
            print()
        else:
            print("\nРецептов нет")

    def display_only_kitchen_name_recipe(self):
        result = self.controller.get_only_kitchen_name_recipe()
        if result:
            print("Кухня:")
            for name in result:
                print(name)
            print()
        else:
            print("\nРецептов нет")

    def display_all_recipe_list(self):
        result = self.controller.get_all_recipe_list()
        if result:
            print(result)
        else:
            print("Данных нет")


    def display_add_recept(self, name_recipe, author, type_dish,
                   tittle, ingredients: list, kitchen_name,
                           filename, user_role='user'):
        result = self.controller.add_recipe(name_recipe, author, type_dish,
                                            tittle, ingredients, kitchen_name,
                                            filename, user_role)
        if result == 'Forbidden':
            print("Forbidden")
        else:
            print(result)