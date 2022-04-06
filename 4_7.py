
def fact(n):
    m = 1
    for el in range(1, n):
        yield m
        m *= el + 1

for el in fact(int(input('Введите число: '))):
    print(el)