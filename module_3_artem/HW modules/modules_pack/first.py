from math import sqrt, cos, log


def my_fn(x):
    y = sqrt((5 - 2 * (x ** 2) + 6 * x) * (cos(x) - log(4 * x)))
    return y


# print(my_fn(5))