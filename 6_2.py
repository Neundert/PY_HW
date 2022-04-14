class Road:
    result = 0
    def __init__(self, h, d, width, length):
        self.h = h
        self.d = d
        self._width = width
        self._length = length
        Road.result = h * d * width * length


a = Road(10,15,20,20)
print(a.result)