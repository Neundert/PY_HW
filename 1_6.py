a = int(input('Расстояние в первый день:'))
b = int(input('Цель:'))
n = 0
while a < b:
    n += 1
    a = 1.1 * a
print ('Дней на достижение цели:',n)