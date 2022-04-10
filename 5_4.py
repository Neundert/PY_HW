str = []
rus = ['Один','Два','Три','Четыре']
with open("text_4.txt", 'r', encoding = 'utf-8') as number:
    for line in number:
        str.append(line.split())

with open("text_4_new.txt", 'w', encoding = 'utf-8') as new_file:
    for i in range(len(str)):
        str[i][0] = rus[i]
        new_file.write(f'{" ".join(str[i])}\n')