my_list = ['jh', 'jszhfg', 'shfmaf']

for index in range(len(my_list)):
    print(index, my_list[index])

for index, value in enumerate(my_list):
    print(index, value)

for enum_value in enumerate(my_list):
    print(enum_value)

# Возвести числа, стоящие на четных местах (начало с 0) в квадрат
# и оставить без изменеия числа н а нечетных местах
my_list = [1, 3, 5, 7, 9]

for index, value in enumerate(my_list):
    if index % 2:
        print(value)
    else:
        print(value ** 2)

# ТАК НЕ ДЕЛАТЬ!
# if index % 2 == 0:
#     print(value ** 2)
# else:
#     print(value)

my_list_str = ['10', '1', '21', '3', '43', '565', '6842']

my_list_int = []
for val in my_list_str:
    my_list_int.append(int(val))
    if int(val) > 20:
        print(val)

# Генераторы списков
# Есть результат выполнения ф-ции
my_list_int = [int(val) for val in my_list_str]
sqr_list = [val ** 2 for val in my_list_int]
print(sqr_list)
# Нет результата выполнения ф-ции
[print(qwe) for qwe in sqr_list]
# Это не имее смысла
result = [print(qwe) for qwe in sqr_list]
print(result)
print(my_list_int)
print(sqr_list)
print(my_list_str)

# Способы использования генератора
my_list_int = [int(value) for value in my_list_str if 2 <= len(value) <= 3]
print(my_list_int)

my_list_int = list(int(value) for value in my_list_str if 2 <= len(value) <= 3)
print(my_list_int)

my_list_int = tuple(int(value) for value in my_list_str if 2 <= len(value) <= 3)
print(my_list_int)

# Множества
str_ = 'qwerty not QWERTY'
my_set = set(str_.lower())
print(len(my_set))
for value in my_set:
    print(value)

print(list(str_))
print(set(str_))
# Методы множеств
str_1 = 'qwerty'
str_2 = 'wrtwty2'
set_1 = set(str_1)
set_2 = set(str_2)
print(set_1.intersection(set_2))
new_set = set_1.union(set_2)
print(set_1)
print(new_set)
set_1.update(set_2)
print(set_1)

my_list = [1, 2, 3, 1, 2, 3, 1, 2, 3]
new_list = list(set(my_list))
print(new_list)

qwe = {1}
print(type(qwe))
# Выбор уникальных символов
my_str = "jhsbdfj,asfkuafbmcnslcjgs,fjhbcjnцапофабрисюлтапфьыорсит"
set_my_str = set(my_str)
for symbol in set_my_str:
    print(f"{symbol}: {my_str.count(symbol)}")

# Словари
key_1 = "asd"
my_dict = {key_1: 123,
           "key_2": 345,
           5: "qwe"}
key = "key_1"
print(my_dict)
print(my_dict[5], my_dict["key_2"])
print(my_dict[key_1])

person = {"Name": "Vova",
          "Age": 40,
          "address": {
              "City": "Dnipro",
              "Street": "Polya"
          }}
# print(person["Name"], person["address"]["City"])
# print(person["LastName"])
person["LastName"] = "Zontov"
person["LastName"] = "ahsfgajwgfja"
person["address"]["building"] = 123
print(person)
