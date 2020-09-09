import time


def print_time(some_func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = some_func(*args, **kwargs)
        print(f"Time: {time.time() - start_time}")
        return res

    return wrapper


@print_time
def my_func_add(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")
    time.sleep(3)
    return num1 + num2


@print_time
def my_func_mult(num1, num2, num3=10):
    print(f"{num1} * {num2} * {num3} = {num1 * num2 * num3}")
    time.sleep(2)


# start_time = time.time()
my_func_add(2, 3)

my_func_mult(3, 4, 5)
# print(f"Time: {time.time() - start_time}")
