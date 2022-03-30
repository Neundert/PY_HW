my_list = input('Введите слова через пробел: ').split(' ')
for i in range(len(my_list)):
    print(i+1,'.',my_list[i][:10])