class Car:
    def __init__(self, speed, colour, name, is_police):
        self.speed = speed
        self.colour = colour
        self.name = name
        self.is_police = True
    def go(self):
        print('Start moving')
    def stop(self):
        print('Stop moving')
    def turn(self, direction):
        self.direction = direction
        print(f'turned onto {self.direction}')
    def show_speed(self, speed):
        self.speed = speed
        print(f'speed:  {self.speed}')

class TownCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        if self.speed < 40:
            print(f'speed:  {self.speed}')
        else:
            print('You have exceeded the speed limit')

class SportCar(Car):
    """Sport"""

class WorkCar(Car):
    def show_speed(self, speed):
        self.speed = speed
        if self.speed < 40:
            print(f'speed:  {self.speed}')
        else:
            print('You have exceeded the speed limit')

class PoliceCar(Car):
    """police"""

main = Car(80, 'black', 'Corolla', False)
print(f'{main.name}:')
main.go()
town = TownCar(70, 'silver', 'Prius', False)
print(f'{town.name}:')
town.show_speed(70)
sport = SportCar(100, 'yellow', 'Lamborghini', False)
print(f'{sport.name}:')
sport.turn('5 avenue')
work = WorkCar(25, 'blue', 'Belarus', False)
print(f'{work.name}:')
work.show_speed(30)
police = PoliceCar(0, 'white', 'Granta', True)
print(f'{police.name}:')
police.stop()