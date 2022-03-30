my_list  = []
new_list = []
q = int(input('Количество элементов: '))
for i in range(q):
    my_list.append(input(f'Элемент списка {i}: '))
print (my_list)
for i in range(0,q-1,2):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]

print (my_list)