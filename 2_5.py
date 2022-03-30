my_list = [7, 5, 3, 3, 2]
n = int(input('Введите число:'))
for i in range(1,len(my_list)):
    if n > my_list[0]:
        my_list.insert(0, n)
        break
    elif my_list[i-1] >= n > my_list[i]:
        my_list.insert(i, n)
        break
    elif n <= my_list[-1]:
        my_list.append(n)
        break

print(my_list)