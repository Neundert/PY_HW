import itertools


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        c = [[a + b for a,b in zip(*x)] for x in zip(self.matrix, other.matrix)]
        return '\n'.join([''.join(['%d\t' % i for i in j]) for j in c])


    def __str__(self):
        return '\n'.join([''.join(['%d\t' % i for i in row]) for row in self.matrix])


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m_1)
m_2 = Matrix([[10, 20, 30], [40, 50, 60],[70, 80,90]])
print(m_2)
print(m_1 + m_2)

