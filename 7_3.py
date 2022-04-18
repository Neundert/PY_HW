class Cell:
    def __init__(self, q):
        self.q = q

    def __add__(self, other):
        return self.q + other.q

    def __sub__(self, other):
        if self.q < other.q:
            return "Нельзя получить отрицательное значение"
        else:
            return self.q - other.q

    def __mul__(self, other):
        return self.q * other.q

    def __truediv__(self, other):
        return self.q // other.q

    def make_order(self, num):
        a = self.q // num
        b = self.q % num
        return '\n'.join([''.join(['*'*num for i in row]) for row in '*'*a]) + '\n' + '*'*b




c = Cell(10)
d = Cell(20)
print(c + d)
print(c - d)
print(c * d)
print(c / d)
print(c.make_order(3))