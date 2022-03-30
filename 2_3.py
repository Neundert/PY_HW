seasons = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
month = int(input('Введите месяц: '))
for key in seasons:
    if key == month:
        print(seasons[key])

winter = [1,2,12]
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
month = int(input('Введите месяц: '))
if month in winter:
    print('winter')
elif month in spring:
    print('spring')
elif month in summer:
    print('summer')
elif month in autumn:
    print('autumn')
else:
    print('error')
