from abc import ABC, abstractmethod

class Clothes(ABC):
    result = 0

    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    @abstractmethod
    def s(self):
        pass

    def __add__(self, other):
        Clothes.result += self.s + other.s
        return Clothes.result

class Coat(Clothes):
    @property
    def s(self):
        return round(self.v / 6.5 + 0.5)

class Suit(Clothes):
    @property
    def s(self):
        return round((2 * self.h + 0.3) / 100)

c = Coat(46, 170)
su = Suit(46, 170)

print(c.s)
print(su.s)
print(c.s + su.s * 3)
