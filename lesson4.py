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

# value_tup = (1, 2, '3', 4, 5)
# # print(value_tup, type(value_tup))
# print(value_tup[1:3])

# a = 2
# b = 3
qwe = (2, 3)
a, b = qwe
print(f"a={a}, b={b}")
a, b = b, a
print(f"a={a}, b={b}")

