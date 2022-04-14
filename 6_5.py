class Stationery:
    title = 'paint'
    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Обводим линии')

class Pencil(Stationery):
    def draw(self):
        print(f'Делаем набросок')
class Handle(Stationery):
    def draw(self):
        print(f'Добавляем цвет')


main = Stationery()
print(main.title)
main.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
pen = Pen()
pen.draw()
