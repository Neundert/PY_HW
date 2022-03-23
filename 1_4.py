q = int(input('Введите число:'))
max_q = q % 10
while q > 0:
    q = q // 10
    if q % 10 > max_q:
        max_q = q % 10
print(max_q)
