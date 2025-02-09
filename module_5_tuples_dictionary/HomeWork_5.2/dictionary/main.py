from working_json import create_json_file, get_unpacking_json
from levels import get_user_level
from utils import base_program
from rank import get_rank


user_name = input("Здравствуйте, как вас зовут? ")

print("Уровни сложности: ")
print("Легкий")
print("Средений")
print("Тяжелый\n")

choice = input("Выберите уровень сложности: ").replace(' ', '').title()

unpack_json = get_unpacking_json()
test_words = get_user_level(choice, unpack_json)
test_answer = base_program(test_words)
result = get_rank(test_answer, unpack_json)

print(f"\nВаш ранг: {result}\n")

creating_json = create_json_file(user_name, test_answer)











