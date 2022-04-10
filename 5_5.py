str = []
with open("sum_zn.txt", 'w+', encoding = 'utf-8') as new_file:
    string = input('Введите числа: ')
    new_file.write(f"{string}\n")
    str = list(string.split())

summ = 0
for i in range(len(str)):
    summ += float(str[i])

print(summ)