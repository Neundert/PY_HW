with open("for_ex_2.txt", 'w', encoding = 'utf-8') as f:
    while True:
        string = input('Введите текст: ')
        if not string:
            break
        f.write(f"{string}\n")

lines = 0
words = 0

for line in open("for_ex_2.txt", 'r', , encoding = 'utf-8'):
    lines += 1
    position = 'out'
    for symbol in line:
        if symbol != ' ' and position == 'out':
            words += 1
            position = 'in'
        elif symbol == ' ':
            position = 'out'

print("Lines:", lines)
print("Words:", words)