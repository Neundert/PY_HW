def my_func(x, y):
    n = 1
    if x >= 0 and y < 0:
        try:
             for i in range(0, -y):
                 n = n / x
        except ZeroDivisionError:
            return "Division by zero"
        return n
    else:
        return 'Неверный ввод'

n1 = float(input('Введите x: '))
n2 = int(input('Введите y: '))
print(my_func(n1, n2))