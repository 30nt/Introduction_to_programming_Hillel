# result = 1
# try:
#     value = int(input("Введи целое число:"))
#     result = result / value
# except (ValueError, ZeroDivisionError):
#     print("Something wrong!")
# # except ZeroDivisionError:
# #     print("ZeroDivisionError")
#
# print(result)

value_tup = (1, 2, '3', 4, 5)
# # print(value_tup, type(value_tup))
# print("value_tup", value_tup[1:3], value_tup[::-1])

# a = 2
# b = 3
# qwe = (2, 3)
# a, b = qwe
# print(f"a={a}, b={b}")
# a, b = b, a
# print(f"a={a}, b={b}")

# for val in value_tup:
#     print(val, type(val))

# my_list = [1, 2, 3, 4, 5]
#
# print(my_list, type(my_list))
# print(my_list[1], my_list[-1], my_list[::-1])
# my_list[2] = 'qwerty'
# print(my_list)

# my_str = 'sjzbdkasndv/sog.kфиаос.дй епдало]цфвщч'
# result = []
# for symbol in my_str:
#     if symbol in 'eyuioaуеыаоэяию':
#         print(result)
#         result.append(symbol)
# print(result)
# value = result.pop()
#
# print(result, value)

# l1 = [1] * 5
# l2 = [4, 5, 6]
# list_ = l1 + l2
# print(list_*3)

# value_list = list(value_tup)
# print(value_list)
# # value_list[2] = 3
# # value_tup = tuple(value_list)
# # print(value_tup)
# value_list_new = value_list.copy()
# value_list_new[2] = 3
# print(value_list_new)
# print(value_list)

# count = 11
# while count > 0:
#     print("Hello!")
#     count -= 1

# count = 1
# while count <= 10:
#     print(f"Hello, {count}")
#     count += 1

# count = 1
# while True:
#     print(f"Hello, {count}")
#     # count += 1
#     if count >= 10:
#         break
#     count += 1

my_value = 7



# while True:
#     value = int(input("Введи число от 1 до 10 включительно"))
#     if value == my_value:
#         print("УГАДАЛ!!!")
#         break
#     elif value < my_value:
#         print("Я загадал большее число")
#     else:
#         print("Я загадал меньшее число")

exit_flag = True
while exit_flag:
    value = int(input("Введи число от 1 до 10 включительно"))
    if value == my_value:
        print("УГАДАЛ!!!")
        exit_flag = False
    elif value < my_value:
        print("Я загадал большее число")
    else:
        print("Я загадал меньшее число")