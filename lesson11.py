#  сортировка чисел
my_list = [2, 4, -1, -10, 0, 30]
# my_list.sort()  # НЕ возвращает новый объект
# print(my_list)
new_list = sorted(my_list, reverse=True)  # возвращает новый объект
print(new_list)
print(my_list)

# функция сортировки
def first_sort_key(value):
    return len(str(value))

my_list = ['2', '4', 's-1', '-10', 10, '-30', '3', 'ab', 'aabc']
cut_list = [value for value in my_list if type(value) == str]
fix_list = [str(value) for value in my_list]
new_list = sorted(my_list, key=first_sort_key)
print(new_list)


# функция сортировки словаря
def sort_dict_key(value_dict):
    return value_dict["name"]

persons = [{"name": "John", "age": 20},
           {"name": "Jack", "age": 12},
           {"name": "Jacob", "age": 40}]
new_persons = sorted(persons, key=sort_dict_key)
print(new_persons)


# поиск по шаблонам
import re
test_str = "asdgfasdfa(067)-524-20-27sgjsjdfajd 7777777777777777hsgefs`  jsgc`sck` "
# reg_exp = r"\([0-9]{3}\)-[0-9]{3}-[0-9]{2}-[0-9]{2}"
reg_exp = r"[0-9]{3,}"
result = re.findall(reg_exp, test_str)
print(result)

# функция сортировки строк по числовым значениям
def sort_string_key(value_str):
    date = re.findall(r'[0-9]{1,4}', value_str)
    if date:
        date = int(date[0])
    else:
        date = 0
    date = (-1) * date if "до н.э." in value_str else date
    return date

test_list = [
    "1945 - окончание второй мировой войны",
    "988 - крещение Руси",
    "1991 - провозглашение независимости Украины",
    "1073 до н.э. - за тысячу лет до восстания Спартака"
]

new_list = sorted(test_list, key=sort_string_key)
print(new_list)

# Сортировка по частоте
test_list = [1, 2, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3]
res = sorted(test_list, key=test_list.count)
print(res)
