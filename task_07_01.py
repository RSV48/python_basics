class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_str = ''
        max_digit = 0
        line_str = ''
        for line in self.matrix:
            for el in line:
                max_digit = len(str(el)) if len(str(el)) > max_digit else max_digit

        for line in self.matrix:
            for el in line:
                insert_str = ' ' * ((max_digit - len(str(el))) + 2)
                line_str += f'{el} {insert_str}'
            matrix_str += f'{line_str} \n'
            line_str = ''
        return matrix_str

    def __add__(self, other):
        line_m = []
        sum_m = []
        for i in range(len(self.matrix)):
            for el in range(len(self.matrix[i])):
                line_m.append(self.matrix[i][el] + other.matrix[i][el])
            sum_m.append(line_m)
            line_m = []
        return Matrix(sum_m)


a = Matrix([[1, 2, 3], [3, 4000, 5], [6, 7, 8]])
b = Matrix([[1000, 2, 3], [3, 4, 5], [6, 7, 8]])

print(a + b)
