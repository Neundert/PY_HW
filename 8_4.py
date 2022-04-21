class Warehouse:
    def __init__(self, q):
        self.q = q

    dict = {}

    @property
    def into(self):
        dict[Equipment.model] = Equipment.price
        return dict

class Equipment:
    def __init__(self, model, price):
        self.model = model
        self.price = price

class Printer(Equipment):
    def __init__(self, name, price, type, color):
        self.model = model
        self.price = price
        self.type = type
        self.color = color

class Scan(Equipment):
    def __init__(self, name, price, type, color):
        self.model = model
        self.price = price
        self.type = type
        self.color = color

class Xerox(Equipment):
    def __init__(self, name, price, type, color):
        self.model = model
        self.price = price
        self.type = type
        self.color = color

new = Equipment('hp', 3900)
s = Warehouse(5)
print(s.into)