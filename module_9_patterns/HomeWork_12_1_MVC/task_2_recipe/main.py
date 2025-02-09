from  model_recipe import RecipeModel
from  controller_pecipe import RecipeController
from  view_recipe import RecipeView

if __name__ == '__main__':
    filename = r'files\recipe.json'
    model = RecipeModel()
    controller = RecipeController(model)
    view = RecipeView(controller)

    view.display_default_recipe()
    view.display_recipe_auth()
    print()

    model.add_recipe("Паста Карбонара", "Алина Островская",
                     "Второе блюдо", "Легендарная паста карбонара. Не слушайте никого,\n"
                                     " в настоящей карбонаре не бывает сливок. При правильном приготовлении\n"
                                     " вы обязательно почувствуете мягкий сливочный вкус - то,\n"
                                     " за что любят это блюдо. В чем секрет? Попробуйте приготовить спагетти карбонара,\n"
                                     " это просто с нашим рецептом.\n", ["Спагетти - 400 г", "Грудинка варено-копчёная - 200 г"," Яйцо куриное - 1 шт.",
                                                                       "Сыр пармезан - 75 г", "Масло сливочное - 2 ст.ложки"], "Итальянская", filename)
    view.display_recipe_auth()
    print()
    view.display_only_name_recipe()
    print()
    view.display_only_author_recipe()
    view.display_only_ingredients_recipe()
    view.display_only_kitchen_name_recipe()