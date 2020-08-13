# Вида импорта модулей
import string
from random import randint # as rnd

letters = string.ascii_letters
print(letters)

some_int = randint(2, 9)
print(some_int)


# ФУНКЦИИ
def print_something():
    print("Hello, World!!!!!")


# def print_dict(some_dict):
#     print(test_value) # ООООЧЕНЬ ПЛОХОЙ ПОДХОД ИСПОЛЬЗОВАТЬ ПЕРЕМЕННУЮ, ЗАДАННУЮ ВНЕ ФУНКЦИИ!!!
#     for key in some_dict:
#         print(f"'{key}': {some_dict[key]}")

def print_dict(some_dict, test_value):
    test_test = "QWERTY"
    print(test_value)
    for key in some_dict:
        print(f"'{key}': {some_dict[key]}")


print_something()
points_dict = {"A": (1, 2),
               "B": (-2, 4),
               "C": (0, -6)}
test_value = "Я просто строка!"
print_dict(points_dict, test_value)
test_v_1 = "Я не он!"
print_dict(points_dict, test_v_1)
