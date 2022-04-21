class Dev(Exception):
    def __init__(self, div):
        self.div = div

dividend = input('Делимое: ')
divider = input('Делитель: ')

try:
    dividend = float(dividend)
    divider = float(divider)
    if divider == 0:
        raise Dev("Division by zero")
except ValueError:
    print ('Введенные значения не являются числами')
except Dev as err:
    print(err)
else:
    print (dividend / divider)

