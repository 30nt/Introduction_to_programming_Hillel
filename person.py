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

    def _change_name(self):
        raise Exception("This method must override id child class")
