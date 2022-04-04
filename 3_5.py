def sumlist():
    k = 0
    while True:
        sum_1 = input('Введите числа: ').split()
        for i in sum_1:
            if i == 'q':
                return k
            else:
                sum_2 = [int(n) for n in sum_1]
                result = sum(sum_2)
                k +=result
        print(k)

print(sumlist())



