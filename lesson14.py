from person import Person

person_john = Person("John", "01/03/1984", "male")


class Student(Person):

    def __init__(self, name, b_date, sex, faculty):
        super().__init__(name, b_date, sex)
        self._change_name()
        self.faculty = faculty
        self._test_value = self.blabla(name, 2)

    @property
    def test_value(self):
        return self._test_value

    @staticmethod
    def blabla(name, number):
        return name * number

    def _change_name(self):
        if "student " not in self.name:
            self.name = "student " + self.name

    def __test(self):
        print("TEST")


# student_john = Student("John", "01/03/1984", "male", "Math")
#
# print(student_john.name, student_john.get_age(), student_john.faculty)
#
# print(student_john.test_value)

class Employer(Person):
    # def __str__(self):
    #     return f"Name: {self.name}, Age: {self.age}"

    def __repr__(self):
        return f"({self.name}, {self.age})"

    def _change_name(self):
        pass
        # if "employer " not in self.name:
        #     self.name = "employer " + self.name


employer_jane = Employer("Jane", "21/10/2001", "female")
employer_noname = Employer("Jane", "21/10/2001", "female")
print(employer_jane, employer_noname)
# my_list = [employer_jane, employer_jane]
# print(my_list)
print(employer_jane == employer_noname)