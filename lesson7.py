# ПОЗИЦИОННОЕ ИСПОЛЬЗОВАНИЕ
# 1) не меняются
points_tuple = ((1, 2), (-2, 4), (0, -6))
print(points_tuple[1])

# 2a) меняются (частично)
points_list = [(1, 2), (-2, 4), (0, -6)]
# 2б) меняются
points_list_change = [[1, 2], [-2, 4], [0, -6]]

# ИСПОЛЬЗОВАНИЕ ПО ИМЕНИ
points_dict = {"A": (1, 2),
               "B": (-2, 4),
               "C": (0, -6)}
print(points_dict)

# Разные уровни детализации словаря
# points_dict = {"A": {"x": 1, "y": 2},
#                "B": {"x": -2, "y": 4},
#                "C": {"x": 0, "y": -6}}
# print(points_dict["A"]["x"])

# Варианты добавлния элементов в словарь
point_D = (3, 5)
points_dict["D"] = point_D

points_dict.update({"D1": point_D})

d2 = {"D2": point_D}
points_dict.update(d2)

print(points_dict)

# Получение значения из словаря по ключу
value = points_dict["A"]
print(value)

# Задача: Если есть ключ D2, то пропустить, а если нет, то добавить в словарь по ключу D2
test_point = (5, 7)
if points_dict.get("D2") is None:
    points_dict["D2"] = test_point
print(points_dict)
# ОООЧЕНЬ ПЛОХО ТАК ДЕЛАТЬ!!!!!!!
# try:
#     points_dict["D2"]
# except KeyError:
#     points_dict["D2"] = test_point
# print(points_dict)

# Прохождение словаря в цикле идет через ключи
for key in points_dict:
    print(key, points_dict[key])

# Получение списка ключей
print(list(points_dict.keys()))
# Получение списка значений
print(list(points_dict.values()))

