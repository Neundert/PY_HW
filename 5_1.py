with open("new_f.txt", 'a', encoding = 'utf-8') as new_file:
    while True:
        string = input('Введите текст: ')
        if not string:
            break
        new_file.write(f"{string}\n")

