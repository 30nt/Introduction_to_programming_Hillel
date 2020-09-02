persons = [
    {"name": "John", "b_date": "01/03/1984", "sex": "male"},
    {"name": "Jane", "b_date": "21/10/2001", "sex": "female"},
    {"name": "Arnold", "b_date": "11/06/1965", "sex": "male"},
]


class Person:
    count = 0

    def __init__(self, name, b_date, sex):
        self.name = name
        self.b_date = b_date
        self.sex = sex
        Person.count += 1
        self.age = self.get_age()

    def get_age(self):
        year = self.b_date.split('/')[-1]
        return 2020 - int(year)


person1 = Person("John", "01/03/1984", "male")
person2 = Person("Jane", "21/10/2001", "female")
person1.job = 'president'
# age = person1.get_age()
# print(age)
age = person1.age
print(age)


# person2 = Person("Jane", "21/10/2001", "female")
# person3 = Person("Arnold", "11/06/1965", "male")
#
# print(person1.name, person2.name, person3.name)
# print(person1.b_date, person2.b_date, person3.b_date)
# # persons = [person1, person2, person3]
#
# print(Person.count)
# print(person1.count)
# person1.count = 7
# print(person1.count)
# Person.count = 8
# print(person2.count)
# print(person1.count)
