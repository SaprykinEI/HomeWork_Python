from model_shoes import ShoesModel
from controller_shoes import ControllerShoes
from view_shoes import ShoesView

if __name__ == '__main__':
    filename = r'files\shoes_file.json'
    model = ShoesModel()
    controller = ControllerShoes(model)
    view = ShoesView(controller)

    view.display_default_action()
    view.display_shoes_auth('moderator')
    view.display_shoes_auth('admin')
    print()

    model.add_shoes('Мужская', 'кроссовки', "Белый", 12000, "Nike",
                    [43, 44, 45], filename)
    model.add_shoes('Женская', 'туфли', "черный", 20000, "DG",
                    [36, 37, 38], filename)

    view.display_shoes_auth('user')
    view.display_only_brand_list()
    view.display_only_assortment_list()
    view.display_only_color_list()
    view.display_shoes_auth()