def int_func():
    for text in input('Введите текст: ').split():
        n = 0
        for el in text:
            if 97 <= ord(el) <= 122:
                n += 1
        print(text.title() if n == len(text) else 'Err', end=' ')

int_func()