class Cmx:
    def __init__(self, param1, param2):
        self.param = {'x': param1, 'y': param2}

    def __add__(self, other):
        x = self.param['x'] + other.param['x']
        y = self.param['y'] + other.param['y']
        return f"{x} + {y}j"

    def __mul__(self, other):
        x = self.param['x'] * other.param['x'] - self.param['y'] * other.param['y']
        y = self.param['x'] * other.param['y'] + self.param['y'] * other.param['x']
        return f"{x} + {y}j"

    def __str__(self):
        return f"{self.param['x']} + {self.param['y']}j"


a = Cmx(2, 3)
b = Cmx(3, 4)
print(a + b)
print(a * b)
