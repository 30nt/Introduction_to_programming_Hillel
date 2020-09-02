class My15:
    def __init__(self):
        self.my_15 = self.generate_15()
        self.row, self.col = self.get_space()

    def generate_15(self):
        my_15 = [['1', '2', '3', ''],
                 ['5', '6', '7', '8'],
                 ['9', '10', '4', '12'],
                 ['13', '14', '15', '11']]
        return my_15

    def print_15(self):
        for row in self.my_15:
            line = " ".join([f"{val:2}" for val in row])
            print(line)

    def get_space(self):
        row_ = 0
        col_ = 0
        for i, row in enumerate(self.my_15):
            if '' in row:
                row_ = i
                for j, col in enumerate(row):
                    if '' == col:
                        col_ = j
        return row_, col_


my_15 = My15()
my_15.print_15()
print(my_15.row, my_15.col)
