def division():
    try:
        dividend = float(input('Делимое: '))
        divider = float(input('Делитель: '))
        return dividend / divider
    except ZeroDivisionError:
        return "Division by zero"

print(division())

