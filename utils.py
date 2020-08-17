import os


def get_distance(point_1: tuple, point_2: tuple) -> float:
    distance = ((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2) ** 0.5
    return distance


def get_area_gerone(point_1, point_2, point_3) -> float:
    a = get_distance(point_1, point_2)
    b = get_distance(point_1, point_3)
    c = get_distance(point_2, point_3)
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area


if __name__ == "__main__":
    assert abs(get_distance((0, 4), (3, 0)) - 5.0) < 0.01
    print("OK")
    home_list = os.listdir("Homework")
    for filename in home_list:
        print(os.path.join("Homework", filename))
    print(home_list)

    some = ['Homework7.txt', 'Homework6.txt', 'Homework5.txt']
    my_str = "$$$".join(some)
    print(my_str)

