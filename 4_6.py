from itertools import count, cycle
from random import sample

d = int(input())
for el in count(d):
    if el > 100:
        break
    else:
        print(el)

print('*' * 30)

my_list = sample(range(-10, 11), 20)
print(my_list)
с = 0

for el in cycle(my_list):
    if с > len(my_list) - 1:
        break
    print(el)
    с += 1
