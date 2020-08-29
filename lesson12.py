import requests
import json

for i in range(1,10):
# url = "https://cat-fact.herokuapp.com/facts"
# url = "https://www.google.com.ua/"
    url = f"https://declarations.com.ua/search?q=&format=opendata&page={i}"
    response = requests.get(url=url)

    # data = json.loads(response.text)

    data = response.json()
    # print(json.dumps(data, indent=2))
    print(json.dumps(data, indent=2, ensure_ascii=False))




import random

def first_func():
    print("111111")


def second_func():
    print("222222")


def third_func():
    print("333333")

func_dict = {
    1: first_func,
    2: second_func,
    3: third_func
}

rand_value = random.randint(1, 3)
func_dict[rand_value]()
