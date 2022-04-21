class KompleksInt:
    def __init__(self, d, m):
        self._i = m
        self._n = d

    def __add__(self, other):
        return other._n + self._n, other._i + self._i

    def __mul__(self, other):
        return self._n * other._n - self._i * other._i, self._i * other._n + self._n * other._i

c_1 = KompleksInt(2, 1)
c_2 = KompleksInt(5, 7)
print(c_1 + c_2)
print(c_1 * c_2)