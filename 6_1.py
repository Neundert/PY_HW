from time import sleep

class TrafficLight:
    __color = 0
    def running(self):
        i = 0
        while i < 6:
            print(f"\033[31m Красный")
            sleep(7)
            print(f"\033[33m Желтый")
            sleep(2)
            print(f"\033[32m Зеленый")
            sleep(5)
            print(f"\033[33m Желтый")
            sleep(2)
            i += 1

a = TrafficLight()
a.running()