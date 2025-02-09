import random
from first import my_fn

def ran():
    rand = my_fn(random.randint(10, 100))
    return rand


print(my_fn(ran()))