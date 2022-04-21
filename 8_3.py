class ListEx(Exception):
    def __init__(self, run):
        self.run = run

k = []
while True:
    el = input('Введите целое число: ')
    if el == 'q':
        print(k)
        break
    try:
        el = int(el)
        if type(el) is str:
            raise ListEx ('Неверный тип данных. Введите число')
    except ValueError:
        print("Вы ввели не число")
    except ListEx as err:
        print(err)
    else:
        k.append(el)

