# A) Создать функцию, которая принимает строку и печатает ее
# с некоторым кол-вом некоторых символов вначале и в конце строки (один кол-во).
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***
#
# Б)Создать функцию, которая принимает строку и печатает ее
# с некоторыми символами НАД и ПОД строкой. КОЛИЧЕСТВО СИМВОЛОВ * РАВНО КОЛИЧЕСТВУ СИМВОЛОВ В СТРОКЕ
# Пример:
# my_str = 'I'm the string'
# Печатает
# **************
# I'm the string
# **************
#
# В) То же, что Б, но ответ должен выглядеть так:
# ********************
# ***I'm the string***
# ********************
#
def modify_string(my_string: str, symbol="*", number=3):
    my_string = f"{symbol * number}{my_string}{symbol * number}"
    return my_string


def print_modify_string(my_string: str, symbol="*", number=3):
    print(modify_string(my_string, symbol=symbol, number=number))


def print_lines_under_above_string(my_string, symbol="*", modificate_string=False):
    if modificate_string:
        my_string = modify_string(my_string, symbol=symbol)
    add_str = symbol * len(my_string)
    new_str = f"{add_str}\n{my_string}\n{add_str}"
    print(new_str)


print_modify_string("Some string", "%", 5)

print_lines_under_above_string("Some string", "#", modificate_string=False)
print_modify_string("Some string", "$")
print_modify_string("Some string", "%", 5)
print_modify_string("Some string", number=5)
print_modify_string(number=5, my_string="Some string", symbol=".")

# Неопределенное количество аргументов функции
def my_func(*args, **kwargs):
    for val in args:
        print(val)
    print(kwargs)

my_func(1, "234", (1, 3, 4), **{"zxc": 1, "qwe3": 4}, qwe=1,  asd=4)

# Есть такой способ работы с файлом
# file = open("README.md", 'r')
# lines = file.read()
# print(lines)
# file.close()

# Но лучше так:
with open("README.md", 'r') as file:
    lines = file.read()
    # print(lines)

print(lines)
print("Hello!")

with open('test.txt', 'w') as file:
    file.write('Hello!\n')
    file.writelines(["asd", 'sdf'])
    file.write(lines)

# Создание папки
import os

def create_folder(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass

# Сохранение строки в файл
def save_string_to_file(filename, path, data: str):
    filename_with_path = os.path.join(path, filename)
    with open(filename_with_path, 'w') as file:
        file.write(data)


create_folder('tmp')
# Создание строки алфавита
alphabet = [chr(numb) for numb in range(ord('a'), ord('z') + 1)]
alphabet = "".join(alphabet)
save_string_to_file('alphabet.txt', 'tmp', alphabet)

# Создание файлов
for symbol in alphabet:
    save_string_to_file(f'{symbol}.txt', 'tmp', alphabet.replace(symbol, symbol.upper()))

# Чтение файлов из папки
tmp_folder = sorted(os.listdir('tmp'), reverse=True)
# Удаление половины случайных файлов
for file in list(set(tmp_folder))[:len(tmp_folder)//2]:
    os.remove(os.path.join('tmp', file))