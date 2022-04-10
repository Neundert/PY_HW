
with open("text_6.txt", 'r', encoding = 'utf-8') as new_f:
    new_result = new_f.readlines()
    for j in new_result:
        new_1 = ''.join((i if i in '1234567890' else ' ') for i in j)
        new_2 = [int(i) for i in new_1.split()]
        print(f'{j.split()[0]} {sum(new_2)}')