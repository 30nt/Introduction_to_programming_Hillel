# from utils import * # импортируй все из файла
from utils import get_distance, get_area_gerone

point_A = (10, 1)
point_B = (10, 2)
point_C = (9, 1)

get_distance(point_A, point_B)
dist_A_B = get_distance(point_A, point_B)
print(dist_A_B)

area_a_b_c = get_area_gerone(point_A, point_B, point_C)

# сравнение двух чисел типа float
if abs(area_a_b_c - 0.5) < 0.001:
    print("OK")
else:
    print("Not OK")

assert abs(area_a_b_c - 0.5) < 0.001  # Если True, то программа идет дальше
assert abs(get_area_gerone((0, 0), (0, 4), (3, 0)) - 6.0) < 0.001
assert abs(get_distance((0, 4), (3, 0)) - 5.0) < 0.01
print(area_a_b_c)


my_dict = {4: 4, 6: 2, 2: 3}

my_sorted = sorted(my_dict)
print(my_sorted)

