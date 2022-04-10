str = []
salaries = []

with open("text_3.txt", 'r', encoding = 'utf-8') as salary:
    for line in salary:
        str = list(line.split())
        salaries.append(float(str[1]))
        if float(str[1]) < 20000:
            print(str[0])

avg = sum(salaries) / len(salaries)
print (f'Средняя зарплата: {avg}')
