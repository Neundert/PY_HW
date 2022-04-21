class Date:
    def __init__(self, date):
        Date.date = date

    @classmethod
    def rename(cls):
        try:
            dd = int(cls.date[:2])
            mm = int(cls.date[3:5])
            yyyy = int(cls.date[-4:])
            cls.valid(dd, mm, yyyy)
        except ValueError:
            print('Ошибка в формате введенных данных. Допустимый формат: ДД-ММ-ГГГГ')
        else:
            return f'День: {dd}\nМесяц: {mm}\nГод: {yyyy}'

    @staticmethod
    def valid(dd, mm, yyyy):
        if 0 < dd < 31 and 0 < mm < 13 and 1899 < yyyy < 2023:
            print('Дата корректна')
        else:
            print('Ошибка в значении "Дата"')

bd = Date('20-11-2020')
print(Date.rename())
