from random import randint

my_list = [randint(-10, 10) for i in range(20)]
print(my_list)

new_list = [i for i in my_list if my_list.count(i) == 1]
print(new_list)
