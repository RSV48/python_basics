class Cell:
    def __init__(self, num):
        self.num = int(num)

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        return abs(self.num - other.num)
        # if self.num > other.num:             часть кода, соответствующая заданию
        #    return self.num - other.num
        # else:
        #    print('Разность количества ячеек клетов меньше нуля')

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return self.num // other.num

    def make_order(self, cell_line):
        num_line = self.num // cell_line if self.num % cell_line == 0 else self.num // cell_line + 1
        last_line = self.num - (num_line - 1) * cell_line
        i = 0
        while i != num_line:
            if cell_line * (i + 1) < self.num:
                print(f'{"*" * cell_line}')
            else:
                print(f'{"*" * last_line}')
            i += 1


c1 = Cell(12)
c2 = Cell(4)
c3 = Cell(c1 + c2)
c4 = Cell(c1 - c2)
c5 = Cell(c2 / c1)
c6 = Cell(c2 * c1)
c6.make_order(5)
